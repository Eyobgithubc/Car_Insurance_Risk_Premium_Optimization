from scipy.stats import ttest_ind, f_oneway
import numpy as np
def test_risk_differences_between_genders(data):
    data = data.copy() 
    
   
    data = data[(data['TotalPremium'] > 0) & (data['TotalPremium'] != np.inf)]

    data['RiskRate'] = data['TotalClaims'] / data['TotalPremium']

    
    risk_rate_male = data[data['Gender'] == 'Male']['RiskRate'].dropna()
    risk_rate_female = data[data['Gender'] == 'Female']['RiskRate'].dropna()
    

    if len(risk_rate_male) > 0 and len(risk_rate_female) > 0:
  

        if risk_rate_male.std() > 0 and risk_rate_female.std() > 0:
            
            t_stat, p_value = ttest_ind(risk_rate_male, risk_rate_female, equal_var=False)  # Assuming unequal variances

            print("T-Test for Risk Differences Between Genders:")
            print(f"T-Statistic: {t_stat:.3f}")
            print(f"P-Value: {p_value:.3f}")

            if p_value < 0.05:
                print("Reject the null hypothesis: Significant risk differences between genders")
            else:
                print("Fail to reject the null hypothesis: No significant risk differences between genders")
        else:
            print("Insufficient variability in risk rates.")
    else:
        print("Insufficient data for t-test.")
