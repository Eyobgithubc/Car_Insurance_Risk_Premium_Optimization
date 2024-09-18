import pandas as pd
from scipy.stats import ttest_ind, f_oneway
def test_margin_differences_between_zip_codes(data):

    data = data.copy()  
    data['ProfitMargin'] = data['TotalPremium'] - data['TotalClaims']

    zip_codes = data['PostalCode'].unique()
    profit_margin_by_zip_code = [data[data['PostalCode'] == zip_code]['ProfitMargin'].dropna() for zip_code in zip_codes]

   
    f_stat, p_value = f_oneway(*profit_margin_by_zip_code)

    print("ANOVA for Margin (Profit) Differences Between Zip Codes:")
    print(f"F-Statistic: {f_stat:.3f}")
    print(f"P-Value: {p_value:.3f}")

    if p_value < 0.05:
        print("Reject the null hypothesis: Significant margin differences between zip codes")
    else:
        print("Fail to reject the null hypothesis: No significant margin differences between zip codes")
