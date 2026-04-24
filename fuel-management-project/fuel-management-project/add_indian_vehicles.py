#!/usr/bin/env python3
"""
Script to add Indian vehicle data to the existing dataset
"""

import pandas as pd
import numpy as np

def add_indian_vehicles():
    """Add Indian vehicle data to the existing dataset"""
    
    # Load existing dataset
    df = pd.read_csv('data/vehicles.csv')
    print(f"Original dataset size: {len(df)}")
    
    # Indian vehicle data (representative samples)
    indian_vehicles = [
        # Maruti Suzuki
        {'year': 2023, 'make': 'Maruti Suzuki', 'model': 'Swift', 'cylinders': 4, 'displ': 1.2, 'drive': 'Front-Wheel Drive', 'trany': 'Manual 5-spd', 'fuelType': 'Regular', 'comb08': 35, 'city08': 33, 'highway08': 38},
        {'year': 2023, 'make': 'Maruti Suzuki', 'model': 'Baleno', 'cylinders': 4, 'displ': 1.2, 'drive': 'Front-Wheel Drive', 'trany': 'Manual 5-spd', 'fuelType': 'Regular', 'comb08': 34, 'city08': 32, 'highway08': 37},
        {'year': 2023, 'make': 'Maruti Suzuki', 'model': 'Dzire', 'cylinders': 4, 'displ': 1.2, 'drive': 'Front-Wheel Drive', 'trany': 'Manual 5-spd', 'fuelType': 'Regular', 'comb08': 33, 'city08': 31, 'highway08': 36},
        {'year': 2023, 'make': 'Maruti Suzuki', 'model': 'WagonR', 'cylinders': 4, 'displ': 1.0, 'drive': 'Front-Wheel Drive', 'trany': 'Manual 5-spd', 'fuelType': 'Regular', 'comb08': 36, 'city08': 34, 'highway08': 39},
        {'year': 2023, 'make': 'Maruti Suzuki', 'model': 'Ertiga', 'cylinders': 4, 'displ': 1.5, 'drive': 'Front-Wheel Drive', 'trany': 'Manual 5-spd', 'fuelType': 'Regular', 'comb08': 28, 'city08': 26, 'highway08': 31},
        
        # Tata Motors
        {'year': 2023, 'make': 'Tata', 'model': 'Nexon', 'cylinders': 4, 'displ': 1.2, 'drive': 'Front-Wheel Drive', 'trany': 'Manual 5-spd', 'fuelType': 'Regular', 'comb08': 30, 'city08': 28, 'highway08': 33},
        {'year': 2023, 'make': 'Tata', 'model': 'Tiago', 'cylinders': 3, 'displ': 1.2, 'drive': 'Front-Wheel Drive', 'trany': 'Manual 5-spd', 'fuelType': 'Regular', 'comb08': 32, 'city08': 30, 'highway08': 35},
        {'year': 2023, 'make': 'Tata', 'model': 'Altroz', 'cylinders': 3, 'displ': 1.2, 'drive': 'Front-Wheel Drive', 'trany': 'Manual 5-spd', 'fuelType': 'Regular', 'comb08': 31, 'city08': 29, 'highway08': 34},
        {'year': 2023, 'make': 'Tata', 'model': 'Harrier', 'cylinders': 4, 'displ': 2.0, 'drive': 'Front-Wheel Drive', 'trany': 'Manual 6-spd', 'fuelType': 'Regular', 'comb08': 25, 'city08': 23, 'highway08': 28},
        {'year': 2023, 'make': 'Tata', 'model': 'Safari', 'cylinders': 4, 'displ': 2.0, 'drive': 'Front-Wheel Drive', 'trany': 'Manual 6-spd', 'fuelType': 'Regular', 'comb08': 24, 'city08': 22, 'highway08': 27},
        
        # Mahindra
        {'year': 2023, 'make': 'Mahindra', 'model': 'Thar', 'cylinders': 4, 'displ': 2.0, 'drive': '4-Wheel Drive', 'trany': 'Manual 6-spd', 'fuelType': 'Regular', 'comb08': 22, 'city08': 20, 'highway08': 25},
        {'year': 2023, 'make': 'Mahindra', 'model': 'XUV700', 'cylinders': 4, 'displ': 2.0, 'drive': 'Front-Wheel Drive', 'trany': 'Automatic 6-spd', 'fuelType': 'Regular', 'comb08': 23, 'city08': 21, 'highway08': 26},
        {'year': 2023, 'make': 'Mahindra', 'model': 'Scorpio', 'cylinders': 4, 'displ': 2.2, 'drive': 'Rear-Wheel Drive', 'trany': 'Manual 6-spd', 'fuelType': 'Regular', 'comb08': 21, 'city08': 19, 'highway08': 24},
        {'year': 2023, 'make': 'Mahindra', 'model': 'Bolero', 'cylinders': 4, 'displ': 1.5, 'drive': 'Rear-Wheel Drive', 'trany': 'Manual 5-spd', 'fuelType': 'Regular', 'comb08': 26, 'city08': 24, 'highway08': 29},
        
        # Hyundai India
        {'year': 2023, 'make': 'Hyundai', 'model': 'i20', 'cylinders': 4, 'displ': 1.2, 'drive': 'Front-Wheel Drive', 'trany': 'Manual 5-spd', 'fuelType': 'Regular', 'comb08': 33, 'city08': 31, 'highway08': 36},
        {'year': 2023, 'make': 'Hyundai', 'model': 'Creta', 'cylinders': 4, 'displ': 1.5, 'drive': 'Front-Wheel Drive', 'trany': 'Manual 6-spd', 'fuelType': 'Regular', 'comb08': 29, 'city08': 27, 'highway08': 32},
        {'year': 2023, 'make': 'Hyundai', 'model': 'Venue', 'cylinders': 4, 'displ': 1.0, 'drive': 'Front-Wheel Drive', 'trany': 'Manual 5-spd', 'fuelType': 'Regular', 'comb08': 34, 'city08': 32, 'highway08': 37},
        {'year': 2023, 'make': 'Hyundai', 'model': 'Verna', 'cylinders': 4, 'displ': 1.5, 'drive': 'Front-Wheel Drive', 'trany': 'Manual 6-spd', 'fuelType': 'Regular', 'comb08': 28, 'city08': 26, 'highway08': 31},
        
        # Kia India
        {'year': 2023, 'make': 'Kia', 'model': 'Seltos', 'cylinders': 4, 'displ': 1.5, 'drive': 'Front-Wheel Drive', 'trany': 'Manual 6-spd', 'fuelType': 'Regular', 'comb08': 30, 'city08': 28, 'highway08': 33},
        {'year': 2023, 'make': 'Kia', 'model': 'Sonet', 'cylinders': 4, 'displ': 1.0, 'drive': 'Front-Wheel Drive', 'trany': 'Manual 5-spd', 'fuelType': 'Regular', 'comb08': 32, 'city08': 30, 'highway08': 35},
        {'year': 2023, 'make': 'Kia', 'model': 'Carnival', 'cylinders': 4, 'displ': 2.0, 'drive': 'Front-Wheel Drive', 'trany': 'Automatic 8-spd', 'fuelType': 'Regular', 'comb08': 24, 'city08': 22, 'highway08': 27},
        
        # Honda India
        {'year': 2023, 'make': 'Honda', 'model': 'City', 'cylinders': 4, 'displ': 1.5, 'drive': 'Front-Wheel Drive', 'trany': 'Manual 5-spd', 'fuelType': 'Regular', 'comb08': 31, 'city08': 29, 'highway08': 34},
        {'year': 2023, 'make': 'Honda', 'model': 'Amaze', 'cylinders': 4, 'displ': 1.2, 'drive': 'Front-Wheel Drive', 'trany': 'Manual 5-spd', 'fuelType': 'Regular', 'comb08': 33, 'city08': 31, 'highway08': 36},
        {'year': 2023, 'make': 'Honda', 'model': 'WR-V', 'cylinders': 4, 'displ': 1.2, 'drive': 'Front-Wheel Drive', 'trany': 'Manual 5-spd', 'fuelType': 'Regular', 'comb08': 32, 'city08': 30, 'highway08': 35},
        
        # Toyota India
        {'year': 2023, 'make': 'Toyota', 'model': 'Innova', 'cylinders': 4, 'displ': 2.0, 'drive': 'Rear-Wheel Drive', 'trany': 'Manual 5-spd', 'fuelType': 'Regular', 'comb08': 26, 'city08': 24, 'highway08': 29},
        {'year': 2023, 'make': 'Toyota', 'model': 'Fortuner', 'cylinders': 4, 'displ': 2.8, 'drive': '4-Wheel Drive', 'trany': 'Manual 6-spd', 'fuelType': 'Regular', 'comb08': 20, 'city08': 18, 'highway08': 23},
        {'year': 2023, 'make': 'Toyota', 'model': 'Glanza', 'cylinders': 4, 'displ': 1.2, 'drive': 'Front-Wheel Drive', 'trany': 'Manual 5-spd', 'fuelType': 'Regular', 'comb08': 34, 'city08': 32, 'highway08': 37},
        
        # Renault India
        {'year': 2023, 'make': 'Renault', 'model': 'Kwid', 'cylinders': 3, 'displ': 1.0, 'drive': 'Front-Wheel Drive', 'trany': 'Manual 5-spd', 'fuelType': 'Regular', 'comb08': 35, 'city08': 33, 'highway08': 38},
        {'year': 2023, 'make': 'Renault', 'model': 'Duster', 'cylinders': 4, 'displ': 1.5, 'drive': 'Front-Wheel Drive', 'trany': 'Manual 5-spd', 'fuelType': 'Regular', 'comb08': 30, 'city08': 28, 'highway08': 33},
        
        # Nissan India
        {'year': 2023, 'make': 'Nissan', 'model': 'Magnite', 'cylinders': 3, 'displ': 1.0, 'drive': 'Front-Wheel Drive', 'trany': 'Manual 5-spd', 'fuelType': 'Regular', 'comb08': 34, 'city08': 32, 'highway08': 37},
        {'year': 2023, 'make': 'Nissan', 'model': 'Kicks', 'cylinders': 4, 'displ': 1.3, 'drive': 'Front-Wheel Drive', 'trany': 'Manual 5-spd', 'fuelType': 'Regular', 'comb08': 31, 'city08': 29, 'highway08': 34},
    ]
    
    # Create DataFrame for Indian vehicles
    indian_df = pd.DataFrame(indian_vehicles)
    
    # Add missing columns to match the original dataset structure
    for col in df.columns:
        if col not in indian_df.columns:
            indian_df[col] = np.nan
    
    # Ensure the Indian vehicles have the same column order
    indian_df = indian_df[df.columns]
    
    # Append Indian vehicles to the main dataset
    df_extended = pd.concat([df, indian_df], ignore_index=True)
    
    # Save the extended dataset
    df_extended.to_csv('data/vehicles.csv', index=False)
    
    print(f"Added {len(indian_vehicles)} Indian vehicles")
    print(f"New dataset size: {len(df_extended)}")
    
    # Show Indian makes in the updated dataset
    indian_makes = sorted(df_extended['make'].unique())
    indian_brands = [make for make in indian_makes if any(brand in str(make).lower() for brand in ['maruti', 'tata', 'mahindra', 'hyundai', 'kia', 'honda', 'toyota', 'renault', 'nissan'])]
    print(f"Indian brands now available: {indian_brands}")

if __name__ == "__main__":
    add_indian_vehicles()
