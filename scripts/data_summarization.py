from IPython.display import display

def data_summarization(data):
  

    numerical_columns = ['TotalPremium', 'TotalClaims', 'SumInsured', 'CalculatedPremiumPerTerm']
    categorical_columns = ['Province', 'PostalCode', 'CoverCategory', 'CoverType', 'Gender']
    vehicle_columns = ['mmcode', 'VehicleType', 'make', 'Model', 'Cylinders', 'cubiccapacity', 
                       'kilowatts', 'bodytype', 'NumberOfDoors', 'VehicleIntroDate']
    
    summary_numerical = data[numerical_columns].describe()
   
    unique_counts = data[categorical_columns].nunique()
    unique_vehicles = data[vehicle_columns].nunique()

    print("Numerical Data Summary:")
    display(summary_numerical)
    
    print("\nUnique Values Count for Categorical Columns:")
    display(unique_counts)
    
    print("\nUnique Values Count for vehicle Columns:")
    display(unique_vehicles)

