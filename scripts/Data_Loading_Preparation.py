import pandas as pd

def clean_data(file_path):
   
    data = pd.read_csv(file_path, delimiter='|')
    print("Data Loaded Successfully!")

    numeric_columns_with_commas = ['TotalPremium', 'TotalClaims', 'SumInsured', 'CalculatedPremiumPerTerm', 'CapitalOutstanding']
    for col in numeric_columns_with_commas:
        data[col] = data[col].astype(str).str.replace(',', '').astype(float)

    categorical_columns = ['MaritalStatus', 'Gender', 'Bank', 'AccountType']
    for col in categorical_columns:
        mode_value = data[col].mode()[0]  
        data[col] = data[col].fillna(mode_value)

    vehicle_columns = ['mmcode', 'VehicleType', 'make', 'Model', 'Cylinders', 'cubiccapacity', 
                       'kilowatts', 'bodytype', 'NumberOfDoors', 'VehicleIntroDate']
    for col in vehicle_columns:
        mode_value = data[col].mode()[0]
        data[col] = data[col].fillna(mode_value)

    data['CapitalOutstanding'] = data['CapitalOutstanding'].fillna(data['CapitalOutstanding'].median())

   
    high_missing_cols = ['CustomValueEstimate', 'NewVehicle', 'WrittenOff', 
                         'Rebuilt', 'Converted', 'CrossBorder', 'NumberOfVehiclesInFleet']
    data[high_missing_cols] = data[high_missing_cols].fillna(0)

    remaining_missing_values = data.isnull().sum()
    print("Remaining Missing Values:\n", remaining_missing_values[remaining_missing_values > 0])
  
    return data
