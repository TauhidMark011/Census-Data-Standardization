import pandas as pd
from pymongo import MongoClient
import mysql.connector

# Step 1: Connect to MongoDB and Fetch Data
client = MongoClient("mongodb://localhost:27017/")
db = client["census_data"]  # Connect to MongoDB database
collection = db["census"]  # Connect to MongoDB collection

# Fetch data from MongoDB
data = list(collection.find({}))  # Convert MongoDB documents to a list of dictionaries

# Remove the MongoDB '_id' field to avoid issues in relational DB
for record in data:
    record.pop("_id", None)

# Convert to a pandas DataFrame
df = pd.DataFrame(data)
print("Data fetched from MongoDB successfully!")
print(df.head())  # Verifying the data

# Step 2: Filter relevant columns for task
required_columns = [
    "State/UT",
    "District",
    "Population",
    "Literate_Male",
    "Literate_Female",
    "Households",
    "Households_with_Internet",
    "Hindus",
    "Muslims",
    "Christians",
    "Others_Religions",
    "Primary",
    "Middle",
    "Secondary",
    "Ownership_Owned_Households",
    "Ownership_Rented_Households",
    "Household_size_1_person_Households",
    "Married_couples_1_Households",
    "Households_with_Bicycle",
    "Households_with_Car_Jeep_Van",
    "Households_with_Radio_Transistor",
    "Households_with_Television",
    "Power_Parity_Less_than_Rs_45000",
    "Male_Workers",
    "Female_Workers",
    "LPG_or_PNG_Households",
    "Below_Primary_Education",
    "Primary_Education",
    "Middle_Education",
    "Secondary_Education",
    "Higher_Education",
    "Graduate_Education",
    "Other_Education",
    "Type_of_latrine_facility_Pit_latrine_Households",
    # "Type_of_latrine_facility_Flush_pour_flush_latrine_connected_to_other_system_Households",
    "Type_of_latrine_facility_Other_latrine_Households",
    "Location_of_drinking_water_source_Near_the_premises_Households",
    "Condition_of_occupied_census_houses_Dilapidated_Households",
    "Households_with_separate_kitchen_Cooking_inside_house",
    "Having_bathing_facility_Total_Households",
    "Having_latrine_facility_within_the_premises_Total_Households"
]

# Filter only the columns that exist in the DataFrame
filtered_columns = [col for col in required_columns if col in df.columns]
df_filtered = df[filtered_columns]
print("Filtered Dataframe with relevant columns: ")
print(df_filtered.head())

# Step 3: Connect to MySQL
mysql_connection = mysql.connector.connect(
    host="localhost",     # MySQL server host
    user="root",          # Your MySQL username
    password="1438011",  # Your MySQL password
    database="census_standardization"  # MySQL database name
)
cursor = mysql_connection.cursor()

# Optimize Column Data Types for MySQL
columns = ", ".join([
    f"`{col}` INT" if "Population" in col or "Rate" in col or "Size" in col
    else f"`{col}` VARCHAR(100)"
    for col in df_filtered.columns
])

# Step 4: Drop the Table (if it exists) and Create a New Table in MySQL
table_name = "census_filtered"
cursor.execute(f"DROP TABLE IF EXISTS {table_name}")  # Ensure no leftover table exists

create_table_query = f"""
CREATE TABLE {table_name} (
    {columns},
    PRIMARY KEY (`State/UT`, `District`)
);
"""
print("Create Table Query:")
print(create_table_query)
cursor.execute(create_table_query)
print(f"Table '{table_name}' created successfully!")

# Step 5: Insert Data into MySQL Table
insert_query = f"""
INSERT INTO {table_name} ({', '.join(f'`{col}`' for col in df_filtered.columns)})
VALUES ({', '.join(['%s'] * len(df_filtered.columns))});
"""

# Insert data row by row
for _, row in df_filtered.iterrows():
    cursor.execute(insert_query, tuple(row))

# Commit changes and close connections
mysql_connection.commit()
cursor.close()
mysql_connection.close()
print("Data uploaded to MySQL successfully!")