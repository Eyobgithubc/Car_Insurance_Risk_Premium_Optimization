import matplotlib.pyplot as plt
import seaborn as sns
def outlier_detection(data):
   

    sns.boxplot(data['TotalPremium'])
    plt.title('Boxplot of TotalPremium')
    plt.show()

    sns.boxplot(data['TotalClaims'])
    plt.title('Boxplot of TotalClaims')
    plt.show()
