from scipy.stats import f_oneway
import matplotlib.pyplot as plt

def analyze_risk_rate_by_province(data):
   
    data.loc[data['TotalPremium'] > 0, 'RiskRate'] = data['TotalClaims'] / data['TotalPremium']
    
    
    provinces = data['Province'].unique()
    risk_rates_by_province = [data[data['Province'] == province]['RiskRate'].dropna() for province in provinces]
    
   
    f_stat, p_value_provinces = f_oneway(*risk_rates_by_province)
    
 
    print("ANOVA for Risk Differences Across Provinces:")
    print(f"F-Statistic: {f_stat:.3f}")
    print(f"P-Value: {p_value_provinces:.3f}")
    
  
    if p_value_provinces < 0.05:
        print("Reject the null hypothesis: Significant risk differences across provinces")
    else:
        print("Fail to reject the null hypothesis: No significant risk differences across provinces")



def plot_average_risk_by_province(data):
   
    
    
    data.loc[data['TotalPremium'] > 0, 'RiskRate'] = data['TotalClaims'] / data['TotalPremium']
    

    average_risk_by_province = data.groupby('Province')['RiskRate'].mean()
    
   
    plt.figure(figsize=(12, 6))
    average_risk_by_province.plot(kind='bar')
    plt.xlabel('Province')
    plt.ylabel('Average Risk Rate')
    plt.title('Average Risk Rate by Province')
    plt.xticks(rotation=90)
    plt.show()
