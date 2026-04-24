#!/usr/bin/env python3
"""
Quick model training script for car mileage prediction.
This script trains the Random Forest model and saves it for the Django web app.
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib
import warnings
warnings.filterwarnings('ignore')

def main():
    print("Loading dataset...")
    df = pd.read_csv('data/vehicles.csv')
    
    # Select key features
    key_features = ['year', 'make', 'model', 'cylinders', 'displ', 'drive', 
                   'trany', 'fuelType', 'comb08', 'city08', 'highway08']
    df_subset = df[key_features].copy()
    
    print(f"Dataset shape: {df_subset.shape}")
    
    # Data cleaning
    key_columns = ['year', 'cylinders', 'displ', 'drive', 'trany', 'fuelType', 'comb08']
    df_clean = df_subset.dropna(subset=key_columns)
    
    # Filter unrealistic values
    df_clean = df_clean[
        (df_clean['comb08'] > 0) & 
        (df_clean['comb08'] < 150) & 
        (df_clean['cylinders'] > 0) & 
        (df_clean['displ'] > 0)
    ]
    
    # Convert MPG to KMPL
    df_clean['comb_kmpl'] = df_clean['comb08'] * 0.425144
    
    # Encode categorical variables
    label_encoders = {}
    categorical_columns = ['drive', 'trany', 'fuelType']
    
    for col in categorical_columns:
        le = LabelEncoder()
        df_clean[col + '_encoded'] = le.fit_transform(df_clean[col].astype(str))
        label_encoders[col] = le
    
    # Create age feature
    current_year = 2024
    df_clean['car_age'] = current_year - df_clean['year']
    
    # Select features for modeling
    feature_columns = ['year', 'car_age', 'cylinders', 'displ', 
                      'drive_encoded', 'trany_encoded', 'fuelType_encoded']
    
    X = df_clean[feature_columns]
    y = df_clean['comb_kmpl']
    
    print(f"Feature matrix shape: {X.shape}")
    print(f"Target vector shape: {y.shape}")
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Train model
    print("Training Random Forest model...")
    rf_model = RandomForestRegressor(
        n_estimators=100,
        max_depth=20,
        min_samples_split=5,
        min_samples_leaf=2,
        random_state=42
    )
    
    rf_model.fit(X_train, y_train)
    
    # Evaluate model
    from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
    
    y_pred = rf_model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    mae = mean_absolute_error(y_test, y_pred)
    
    print(f"Model Performance:")
    print(f"R² Score: {r2:.4f}")
    print(f"RMSE: {rmse:.4f} KMPL ({rmse/0.425144:.2f} MPG)")
    print(f"MAE: {mae:.4f} KMPL ({mae/0.425144:.2f} MPG)")
    
    # Save model and preprocessing objects
    model_data = {
        'model': rf_model,
        'label_encoders': label_encoders,
        'feature_columns': feature_columns,
        'scaler': None,
        'target_column': 'comb_kmpl'
    }
    
    joblib.dump(model_data, 'models/car_mileage_rf_model.joblib')
    print("Model saved successfully to models/car_mileage_rf_model.joblib")
    
    # Test sample prediction
    sample_car = {
        'year': 2022,
        'cylinders': 4,
        'displ': 2.0,
        'drive': 'Front-Wheel Drive',
        'trany': 'Automatic 5-spd',
        'fuelType': 'Regular'
    }
    
    car_age = current_year - sample_car['year']
    drive_encoded = label_encoders['drive'].transform([sample_car['drive']])[0]
    trany_encoded = label_encoders['trany'].transform([sample_car['trany']])[0]
    fuel_encoded = label_encoders['fuelType'].transform([sample_car['fuelType']])[0]
    
    sample_features = [[
        sample_car['year'], car_age, sample_car['cylinders'], 
        sample_car['displ'], drive_encoded, trany_encoded, fuel_encoded
    ]]
    
    predicted_kmpl = rf_model.predict(sample_features)[0]
    predicted_mpg = predicted_kmpl / 0.425144
    
    print(f"\nSample prediction for 2022 car (4 cylinders, 2.0L):")
    print(f"Predicted KMPL: {predicted_kmpl:.2f}")
    print(f"Predicted MPG: {predicted_mpg:.2f}")

if __name__ == "__main__":
    main()
