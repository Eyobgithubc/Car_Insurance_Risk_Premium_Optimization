import matplotlib.pyplot as plt
import seaborn as sns
def univariate_analysis(data):
 
    plt.hist(data['TotalPremium'], bins=30)
    plt.title('Distribution of TotalPremium')
    plt.xlabel('TotalPremium')
    plt.ylabel('Frequency')
    plt.show()
    
    sns.countplot(x='Province', data=data)
    plt.title('Distribution of Insurance by Province')
    plt.xticks(rotation=90)
    plt.show()
