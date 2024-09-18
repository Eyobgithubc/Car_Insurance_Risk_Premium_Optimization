import matplotlib.pyplot as plt
import seaborn as sns

def univariate_analysis(data):
    # Existing columns
    numeric_columns_with_commas = ['TotalPremium', 'TotalClaims', 'SumInsured', 'CalculatedPremiumPerTerm', 'CapitalOutstanding']
    categorical_columns = ['MaritalStatus', 'Gender', 'Bank', 'AccountType']
    
    # Vehicle-related columns
    vehicle_columns = ['mmcode', 'VehicleType', 'make', 'Model', 'Cylinders', 'cubiccapacity', 
                       'kilowatts', 'bodytype', 'NumberOfDoors', 'VehicleIntroDate']

    # Plot histograms for each numeric column
    for column in numeric_columns_with_commas:
        plt.figure(figsize=(10, 6))
        plt.hist(data[column].replace({',': ''}, regex=True).astype(float), bins=30)
        plt.title(f'Distribution of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.show()
    
    # Plot countplot for the 'Province' column
    plt.figure(figsize=(10, 6))
    sns.countplot(x='Province', data=data)
    plt.title('Distribution of Insurance by Province')
    plt.xticks(rotation=90)
    plt.show()
    
    # Plot bar charts for each categorical column
    for column in categorical_columns:
        plt.figure(figsize=(10, 6))
        sns.countplot(x=column, data=data)
        plt.title(f'Distribution of {column}')
        plt.xticks(rotation=90)
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.show()

    # Plot bar charts for each vehicle-related column
    for column in vehicle_columns:
        plt.figure(figsize=(10, 6))
        sns.countplot(x=column, data=data)
        plt.title(f'Distribution of {column}')
        plt.xticks(rotation=90)
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.show()
