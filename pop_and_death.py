import pandas as pd
import glob
import re

deaths_df = pd.read_csv("all_combined_1x1.csv", sep=",", low_memory=False)
deaths_df["Year"] = deaths_df["Year"].astype("int64")
deaths_df["Age"] = deaths_df["Age"].astype("int64")

result_df = pd.DataFrame(columns=["Country", "Year", "Age", "Female_deaths", "Male_deaths", "Female_population", "Male_population"])

for file in glob.glob("*population.txt"):
    print(file)
    match = re.match(r"(.*)population\.txt", file)
    if match:
        country_code = match.group(1)
        print(f"Processing {country_code}...")

        population_df = pd.read_csv(file, skiprows=3, delim_whitespace=True, names=["Year", "Age", "Female", "Male", "Total"])
        population_df["Year"] = pd.to_numeric(population_df["Year"], errors='coerce')
        population_df.dropna(subset=["Year"], inplace=True)
        population_df = population_df[~population_df["Year"].astype(str).str.contains('[+-]')]
        population_df["Year"] = population_df["Year"].astype("int64")

        population_df["Age"] = population_df["Age"].replace("110+", "110").astype("int64")

        deaths_country_df = deaths_df[deaths_df["Country"] == country_code]

        merged_df = pd.merge(deaths_country_df, population_df, on=["Year", "Age"], suffixes=("_deaths", "_population"))

        if not merged_df.empty:
            print(f"Merged data for {country_code}:")
            print(merged_df.head())

            result_df = pd.concat([result_df, merged_df], ignore_index=True)
        else:
            print(f"No data for {country_code}")
    else:
        print(f"File {file} does not match expected format")
        
result_df.to_csv("final_data.csv", index=False)
