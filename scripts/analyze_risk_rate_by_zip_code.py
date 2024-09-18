import pandas as pd
from scipy.stats import f_oneway

def analyze_risk_by_zip_code(data):
    
 
    data['RiskRate'] = data['TotalClaims'] / data['TotalPremium']
    

    data = data[data['TotalPremium'] > 0]
    
   
    data = data.dropna(subset=['RiskRate'])
    
    zip_codes = data['PostalCode'].unique()
    risk_rates_by_zip_code = [data[data['PostalCode'] == zip_code]['RiskRate'] for zip_code in zip_codes]
   
    risk_rates_by_zip_code = [rates for rates in risk_rates_by_zip_code if len(rates) > 0]
    
    if len(risk_rates_by_zip_code) < 2:
        print("Not enough groups with data to perform ANOVA.")
        return
    
  
    f_stat_zip, p_value_zip = f_oneway(*risk_rates_by_zip_code)
 
    print("ANOVA for Risk Differences Between Zip Codes:")
    print(f"F-Statistic: {f_stat_zip:.3f}")
    print(f"P-Value: {p_value_zip:.3f}")
    
    if p_value_zip < 0.05:
        print("Reject the null hypothesis: Significant risk differences between zip codes")
    else:
        print("Fail to reject the null hypothesis: No significant risk differences between zip codes")



