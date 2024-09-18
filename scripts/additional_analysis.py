import matplotlib.pyplot as plt
import seaborn as sns
def additional_analysis(data):
    """
    Performs additional analysis such as exploring TotalPremium by VehicleType and SumInsured vs TotalPremium.
    """


  
    sns.boxplot(x='VehicleType', y='TotalPremium', data=data)
    plt.title('Premium by Vehicle Type')
    plt.xticks(rotation=90)
    plt.show()

 
    sns.countplot(x='CoverType', data=data)
    plt.title('Distribution of Cover Type')
    plt.xticks(rotation=90)
    plt.show()

  
    sns.scatterplot(x='SumInsured', y='TotalPremium', data=data)
    plt.title('SumInsured vs TotalPremium')
    plt.show()
