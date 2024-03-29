import numpy as np
import pandas as pd

def wave_class(data=None, wave_lengths=None, velocities=None, frequencies=None, return_extreme=None, return_csv=None): 
    
    wave_ranges = {
        (0.1, 3.5): "Delta",
        (4, 8): "Theta",
        (8, 12): "Alpha",
        (12, 15): "Low Beta",
        (15, 18): "Mid Beta",
        (18, np.inf): "High Beta",
        (30, np.inf): "Gamma"
    }

    result = []
    Hzres = []
    for index, row in data.iterrows():
        freq = row['Velocity'] / row['Lambda']
        length = row['Lambda'] / row['Velocity']
        velo = row['Lambda'] * row['Velocity']

        Hzres.append(freq)
        wave_type_found = False  
        
        for (start, end), wave_type in wave_ranges.items():
            if start <= freq < end:
                result.append(wave_type)
                wave_type_found = True
                break
                
        if not wave_type_found:
            
            result.append("NaN")
            
    if frequencies is None:
        data["Frequency(Hz)"] = Hzres
        data['Wave_Class'] = result
    else: 
        data['Wave_Class'] = result
    if return_extreme is True: 
        extreme_df_low = data[(data['Frequency(Hz)'] <= data['Frequency(Hz)'].quantile(0.1))]
        extreme_df_high = data[data['Frequency(Hz)'] >= data['Frequency(Hz)'].quantile(0.9)]

        return data, extreme_df_low.sort_values(by='Frequency(Hz)', ascending=False), extreme_df_high.sort_values(by='Frequency(Hz)', ascending=False)
    elif return_csv is True:
        return data.to_csv('wave_classes.csv', index=False)
    else: 
        return data 
    

