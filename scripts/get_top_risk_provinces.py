def get_top_risk_provinces(data, top_n=5):
   
    
 
    average_risk_by_province = data.groupby('Province')['RiskRate'].mean()
    
   
    sorted_risk_by_province = average_risk_by_province.sort_values()
    
  
    print("Average Risk Rates by Province:")
    print(sorted_risk_by_province)
    
 
    highest_risk_provinces = sorted_risk_by_province.tail(top_n)  
    lowest_risk_provinces = sorted_risk_by_province.head(top_n)   
    
    
    print(f"\nProvinces with Highest Risk Rates (Top {top_n}):")
    print(highest_risk_provinces)
    
    print(f"\nProvinces with Lowest Risk Rates (Top {top_n}):")
    print(lowest_risk_provinces)
    
    return {
        'highest_risk_provinces': highest_risk_provinces,
        'lowest_risk_provinces': lowest_risk_provinces
    }
