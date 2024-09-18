import matplotlib.pyplot as plt
import seaborn as sns
def bivariate_analysis(data):

    corr_matrix = data[['TotalPremium', 'TotalClaims', 'SumInsured', 'CalculatedPremiumPerTerm']].corr()
    sns.heatmap(corr_matrix, annot=True)
    plt.title('Correlation Matrix of Numerical Columns')
    plt.show()

    sns.scatterplot(x='TotalPremium', y='TotalClaims', data=data)
    plt.title('TotalPremium vs TotalClaims')
    plt.show()
