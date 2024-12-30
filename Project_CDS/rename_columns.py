import pandas as pd

file_path = r"census_2011.csv"  # Input file  
output_path = r"census_2011_renamed.csv" #Output file for task 1

#Loading the dataset
census_data = pd.read_csv(file_path)   #function reads the original dataset (census_2011.csv).
#Define the column renaming mapping
columns_to_rename = {
    'State name': 'State/UT',
    'District name': 'District',
    'Male_Literate': 'Literate_Male',
    'Female_Literate': 'Literate_Female',
    'Rural_Households': 'Households_Rural',
    'Urban_ Households': 'Households_Urban',
    'Age_Group_0_29': 'Young_and_Adult',
    'Age_Group_30_49': 'Middle_Aged',
    'Age_Group_50': 'Senior_Citizen',
    'Age not stated': 'Age_Not_Stated'
}
#Apply the renaming 
census_data.rename(columns= columns_to_rename, inplace=True)
#Save the modified dataset 
census_data.to_csv(output_path, index=False)

## Print confirmation and first few rows of the renamed dataset
print("Columns have been renamed successfully..")
print("Renamed Columns:.")
print(census_data.columns)  