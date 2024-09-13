from IPython.display import display

def data_summarization(data):
  

    numerical_columns = ['TotalPremium', 'TotalClaims', 'SumInsured', 'CalculatedPremiumPerTerm']
    categorical_columns = ['Province', 'PostalCode', 'CoverCategory', 'CoverType', 'Gender']
    
    summary_numerical = data[numerical_columns].describe()
   
    unique_counts = data[categorical_columns].nunique()

    print("Numerical Data Summary:")
    display(summary_numerical)
    
    print("\nUnique Values Count for Categorical Columns:")
    display(unique_counts)

