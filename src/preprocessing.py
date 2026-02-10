import pandas as pd
import numpy as np
from sklearn.preprocessing import OrdinalEncoder, MinMaxScaler

def preprocess_student_data(input_path, output_path):
    """
    Processes raw student stress data into a model-ready format.
    - Handles high cardinality (drops Student_ID)
    - Fixes floating point artifacts
    - Manages compositional redundancy (drops one hour feature)
    - Ordinal encodes the target
    - Generates interaction ratios
    - Scales numerical features
    """
    # 1. Load Data
    df = pd.read_csv(input_path)
    
    # 2. Handle High Cardinality
    # Drop Student_ID as it lead to overfitting and has 100% uniqueness
    df = df.drop(columns=['Student_ID'])
    
    # 3. Handle Compositional Data (24-Hour Law)
    hour_cols = [
        'Study_Hours_Per_Day', 
        'Extracurricular_Hours_Per_Day', 
        'Sleep_Hours_Per_Day', 
        'Social_Hours_Per_Day', 
        'Physical_Activity_Hours_Per_Day'
    ]
    
    # Fix minor floating point sums to exactly 24.0
    total_hours = df[hour_cols].sum(axis=1)
    for col in hour_cols:
        df[col] = df[col] * (24.0 / total_hours)
    
    # 4. Feature Engineering: Interaction Ratios
    # Academic Pressure Index
    df['Academic_Pressure_Index'] = df['Study_Hours_Per_Day'] / (df['Social_Hours_Per_Day'] + df['Sleep_Hours_Per_Day'] + 1e-5)
    
    # Wellness Ratio (Physical + Sleep vs Study)
    df['Wellness_Ratio'] = (df['Physical_Activity_Hours_Per_Day'] + df['Sleep_Hours_Per_Day']) / (df['Study_Hours_Per_Day'] + 1e-5)
    
    # GPA Efficiency
    df['GPA_Efficiency'] = df['GPA'] / (df['Study_Hours_Per_Day'] + 1e-5)

    # 5. Redundancy Management
    # Drop one feature to remove linear dependency (Sum=24)
    # Extracurricular is often the least 'risk-defining' in academic datasets
    df = df.drop(columns=['Extracurricular_Hours_Per_Day'])
    
    # 6. Ordinal Encoding (Target)
    # Low=0, Moderate=1, High=2
    stress_order = ['Low', 'Moderate', 'High']
    encoder = OrdinalEncoder(categories=[stress_order])
    df['Stress_Level'] = encoder.fit_transform(df[['Stress_Level']]).astype(int)
    
    # 7. Scaling
    scaler = MinMaxScaler()
    num_cols = df.columns.drop('Stress_Level')
    df[num_cols] = scaler.fit_transform(df[num_cols])
    
    # 8. Save
    df.to_csv(output_path, index=False)
    print(f"Preprocessing complete. Processed data saved to: {output_path}")
    return df

if __name__ == "__main__":
    # Use absolute paths or correct relative paths depending on where it's run
    # For now, we assume it's run from the root or src
    import os
    if not os.path.exists('../data/raw.csv'):
        input_file = './data/raw.csv'
        output_file = './data/processed_student_data.csv'
    else:
        input_file = '../data/raw.csv'
        output_file = '../data/processed_student_data.csv'
    
    preprocess_student_data(input_file, output_file)
