def data_quality_check(data):
    
    remaining_missing_values = data.isnull().sum()
   
    print("Remaining Missing Values:\n", remaining_missing_values[remaining_missing_values > 0])
    
