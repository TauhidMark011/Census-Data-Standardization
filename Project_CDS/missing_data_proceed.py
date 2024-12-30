#(cleaning data + saving to MongoDB)
import pandas as pd
from pymongo import MongoClient
file_path = r"census_2011_updatedStates.csv"
output_path = r"census_2011_missingData_proceed.csv" # Output file for Task 4
#Load the Dataset
census_data = pd.read_csv(file_path)
#Find missing data before 
print("Before: ")
missing_data = census_data.isnull().sum()
missing_percentage = (missing_data / len (census_data)) * 100
print("Missing Data (Before Filling): ")
print(missing_data)
print("\nPercentage of Missing Data (Before Filling): ")
print(missing_percentage)
#Filling misiing data based on rules 
if "Male" in census_data.columns and "Female" in census_data.columns:
    census_data["Population"] = census_data["Population"].fillna(
        #Handling missing sub-columns similarly
        census_data["Male"].fillna(0) + census_data["Female"].fillna(0)
    )
if "Literate_Male" in census_data.columns and "Literate_Female" in census_data.columns:
    census_data["Literate"] = census_data["Literate"].fillna(
        #Handling missing sub-columns similarly
        census_data["Literate_Male"].fillna(0) + census_data["Literate_Female"].fillna(0)   
        )

if set(["Young_and_Adult", "Middle_Aged", "Senior_Citizen", "Age_Not_Stated"]).issubset(census_data.columns):
    census_data["Population"] = census_data["Population"].fillna(
        census_data["Young_and_Adult"] 
        + census_data["Middle_Aged"] 
        + census_data["Senior_Citizen"] 
        + census_data["Age_Not_Stated"]  
    )

if "Households_Rural" in census_data.columns and "Urban_Households" in census_data.columns :
    census_data["Households"] = census_data["Households"].fillna(
                #Handling missing sub-columns similarly
        census_data["Households_Rural"].fillna(0) + census_data["Urban_Households"].fillna(0)
    )  
#Recheck missing data after
print("After: ")
missing_data_after = census_data.isnull().sum()
missing_percentage_after = (missing_data_after / len (census_data)) * 100
print("\nMissing Data (After Filling): ")
#To check how many missing values exist in each of these columns using pandas cmd.
print(census_data[['Population','Literate','Households']].isnull().sum())
print(missing_data_after)
print("\nPercentage Of Missing Data(After Filling): ")
print(missing_percentage_after)
#Save the processed dataset
census_data.to_csv(output_path, index=False)
print("\nMissind data saved and processed successfully!")

#Insert data into MongoDB
client = MongoClient("mongodb://localhost:27017/") #Local MongoDB Connection
db = client["census_data"] #MongoDB server connection.
collection = db["census"]
data_dict = census_data.to_dict(orient = "records")
collection.insert_many(data_dict)
#Verify data insertion
count = collection.count_documents({})
print(f"Numbers of records in the 'census' collection: {count}")
print("Data successfully saved to MongoDB")
#Fetch Data from MongoDB and Upload to MySQL