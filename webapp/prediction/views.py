import joblib
import numpy as np
import pandas as pd
from django.shortcuts import render
from django.http import JsonResponse
import os

# Load the trained model
MODEL_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'models', 'car_mileage_rf_model.joblib')

def load_model():
    """Load the trained model and preprocessing objects"""
    try:
        model_data = joblib.load(MODEL_PATH)
        return model_data
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

def get_form_options():
    """Get options for form dropdowns"""
    try:
        df = pd.read_csv('data/vehicles.csv')
        
        # Get unique values for dropdowns
        drive_options = sorted(df['drive'].dropna().unique())
        trans_options = sorted(df['trany'].dropna().unique())
        fuel_options = sorted(df['fuelType'].dropna().unique())
        
        return {
            'drive_options': drive_options,
            'trans_options': trans_options,
            'fuel_options': fuel_options
        }
    except Exception as e:
        print(f"Error loading form options: {e}")
        return {
            'drive_options': ['Front-Wheel Drive', 'Rear-Wheel Drive', '4-Wheel or All-Wheel Drive'],
            'trans_options': ['Automatic 4-spd', 'Automatic 5-spd', 'Manual 5-spd'],
            'fuel_options': ['Regular', 'Premium', 'Diesel']
        }

def home(request):
    """Home page with prediction form"""
    form_options = get_form_options()
    return render(request, 'prediction/home.html', form_options)

def predict(request):
    """Handle prediction requests"""
    if request.method == 'POST':
        try:
            # Load model
            model_data = load_model()
            if not model_data:
                return JsonResponse({'error': 'Model not available'}, status=500)
            
            model = model_data['model']
            label_encoders = model_data['label_encoders']
            feature_columns = model_data['feature_columns']
            
            # Get form data
            year = int(request.POST.get('year'))
            cylinders = int(request.POST.get('cylinders'))
            displacement = float(request.POST.get('displacement'))
            drive = request.POST.get('drive')
            transmission = request.POST.get('transmission')
            fuel_type = request.POST.get('fuel_type')
            
            # Create car age
            current_year = 2024
            car_age = current_year - year
            
            # Encode categorical variables
            drive_encoded = label_encoders['drive'].transform([drive])[0]
            trans_encoded = label_encoders['trany'].transform([transmission])[0]
            fuel_encoded = label_encoders['fuelType'].transform([fuel_type])[0]
            
            # Create feature array
            features = np.array([[
                year, car_age, cylinders, displacement,
                drive_encoded, trans_encoded, fuel_encoded
            ]])
            
            # Make prediction
            predicted_kmpl = model.predict(features)[0]
            predicted_mpg = predicted_kmpl / 0.425144
            
            # Calculate fuel cost estimate for Indian context
            # Converting to Indian context:
            # 1 USD = 83 INR (approximate exchange rate)
            # Fuel price in India: ~₹102 per liter (petrol)
            # Annual driving: 15,000 km (Indian standard)
            
            # Convert MPG to KMPL (already done in prediction)
            fuel_price_per_liter_inr = 102  # Indian Rupees per liter
            annual_km = 15000  # Annual driving in km (Indian standard)
            annual_fuel_cost = (annual_km / predicted_kmpl) * fuel_price_per_liter_inr
            
            response_data = {
                'success': True,
                'predicted_kmpl': round(predicted_kmpl, 2),
                'predicted_mpg': round(predicted_mpg, 2),
                'annual_fuel_cost': round(annual_fuel_cost, 2),
                'input_data': {
                    'year': year,
                    'cylinders': cylinders,
                    'displacement': displacement,
                    'drive': drive,
                    'transmission': transmission,
                    'fuel_type': fuel_type
                }
            }
            
            return JsonResponse(response_data)
            
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Invalid request method'}, status=400)

def about(request):
    """About page"""
    return render(request, 'prediction/about.html')
