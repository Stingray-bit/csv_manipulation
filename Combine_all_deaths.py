import pandas as pd
import os
from pathlib import Path

def read_and_combine_files(src_dir):
    src_path = Path(src_dir)
    all_data = []

    for file in src_path.iterdir():
        if file.is_file() and file.name.endswith('.txt'):
            country_name = file.stem
            df = pd.read_csv(file, delim_whitespace=True, skiprows=3, header=None, names=['Year', 'Age', 'Female', 'Male', 'Total'])
            df['Country'] = country_name
            all_data.append(df)

    combined_data = pd.concat(all_data, ignore_index=True)
    return combined_data

def save_to_csv(dataframe, dest_file):
    dataframe.to_csv(dest_file, index=False)

source_directory = r"C:\Users\44741\Desktop\all_countries_death_1x1" 
destination_file = r"C:\Users\44741\Desktop\all_countries_death_1x1\all_combined_1x1.csv" 

combined_data = read_and_combine_files(source_directory)
save_to_csv(combined_data, destination_file)
