import pandas as pd

file_path = r"census_2011_state_ut_renamed.csv" #Input file from task 2
output_path = r"census_2011_updatedStates.csv" #Output file for task 3
telangana_districts_path = r"Telangana.txt"
#Load the dataset 
census_data = pd.read_csv(file_path)
#Read the telangana districts from text file
with open(telangana_districts_path, "r") as file:
    #Read all lines from the file 
    lines = file.readlines()
    #creating a list of districts by removing white space from each line
    telangana_districts = []
    for line in lines:
        telangana_districts.append(line.strip())
#Update State/UT for Telagana Districts 
census_data.loc[census_data["District"].isin(telangana_districts), "State/UT"] = "Telangana"

#Update State/UT for Ladakh districts [Leh and kargil]
ladakh_districts = ["Leh(Ladakh)", "Kargil"]
census_data.loc[census_data["District"].isin(ladakh_districts), "State/UT"] = "Ladakh"
#Save the updated data set
census_data.to_csv(output_path, index=False)
        #Print the processed lists of districts
print("List of Telangana districts:", telangana_districts)
print("State/UT updates have been applied successfully!")
print(census_data[census_data["State/UT"].isin(["Telangana", "Ladakh"])].head())