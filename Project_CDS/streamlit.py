import streamlit as st
import mysql.connector
import pandas as pd

# Establish connection to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1438011",
    database="census_standardization"
)
cursor = conn.cursor()

# Query to fetch total population of each district
query_1 = "SELECT `District`, SUM(`Population`) AS Total_Population FROM census_filtered GROUP BY `District`;"
query_2 = "SELECT `District`, SUM(`Literate_Male`) AS Total_Literate_Males, SUM(`Literate_Female`) AS Total_Literate_Females FROM census_filtered GROUP BY `District`;"
#percentage of workers (both male and female) in each district
query_3 = """SELECT `District`, (SUM(`Male_Workers`) + SUM(`Female_Workers`)) AS Total_Workers,
    SUM(`Population`) AS Total_Population, ROUND(((SUM(`Male_Workers`) + SUM(`Female_Workers`)) / SUM(`Population`)) * 100, 2) AS Worker_Percentage
FROM census_filtered
GROUP BY `District`;"""
query_4 = """SELECT `District`, SUM(`LPG_or_PNG_Households`) AS Households_with_LPG_or_PNG
FROM census_filtered GROUP BY `District`;"""
query_5 =  """SELECT `District`, SUM(`Hindus`) AS Total_Hindus, SUM(`Muslims`) AS Total_Muslims, SUM(`Christians`) AS Total_Christians,
SUM(`Others_Religions`) AS Total_Other_Religions
FROM census_filtered
GROUP BY `District`;"""
query_6 = """SELECT `District`, SUM(`Households_with_Internet`) AS Total_Internet_Access_Households
FROM census_filtered GROUP BY `District`;"""
query_7 = """SELECT 
    `District`, 
    SUM(`Below_Primary_Education`) AS Below_Primary_Total, SUM(`Primary_Education`) AS Primary_Total, SUM(`Middle_Education`) AS Middle_Total,
    SUM(`Secondary_Education`) AS Secondary_Total, SUM(`Higher_Education`) AS Higher_Total, SUM(`Graduate_Education`) AS Graduate_Total,
    SUM(`Other_Education`) AS Other_Total FROM census_filtered GROUP BY `District`;"""
query_8 = """SELECT District, SUM(Households_with_Bicycle) AS Bicycle_Households, SUM(Households_with_Car_Jeep_Van) AS Car_Households,
    SUM(Households_with_Radio_Transistor) AS Radio_Households, SUM(Households_with_Television) AS Television_Households FROM census_filtered GROUP BY District;"""
query_9 = """SELECT District,
    SUM(Condition_of_occupied_census_houses_Dilapidated_Households) AS Dilapidated_Houses, SUM(Households_with_separate_kitchen_Cooking_inside_house) AS Separate_Kitchen_Houses,
    SUM(Having_bathing_facility_Total_Households) AS Bathing_Facility_Houses, SUM(Having_latrine_facility_within_the_premises_Total_Households) AS Latrine_Facility_Houses 
    FROM census_filtered GROUP BY District;"""
query_10 ="""SELECT `State/UT`, SUM(`Households`) AS Total_Households
FROM census_filtered GROUP BY `State/UT`;"""
query_11 = """SELECT `State/UT`, SUM(`Having_latrine_facility_within_the_premises_Total_Households`) AS Total_Households_with_Latrine
FROM census_filtered GROUP BY `State/UT`;"""
#Average household size in each state
query_12 = """SELECT `State/UT`, ROUND(SUM(`Population`) / SUM(`Households`), 2) AS Average_Household_Size
FROM census_filtered GROUP BY `State/UT`;"""
query_13 = query_13 = """SELECT `State/UT`, SUM(`Ownership_Owned_Households`) AS Total_Owned_Households, SUM(`Ownership_Rented_Households`) AS Total_Rented_Households
FROM census_filtered GROUP BY `State/UT`;"""
query_14 = """SELECT `State/UT`,SUM(`Type_of_latrine_facility_Pit_latrine_Households`) AS Total_Pit_Latrine, SUM(`Type_of_latrine_facility_Other_latrine_Households`) AS Total_Other_Latrine
FROM census_filtered GROUP BY `State/UT`;"""
query_15 = """SELECT `State/UT`, SUM(`Location_of_drinking_water_source_Near_the_premises_Households`) AS Households_Near_Drinking_Water
FROM census_filtered GROUP BY `State/UT`;"""
# Query to fetch literate population and total population for each State/UT
query_literacy_rate = """
SELECT `State/UT`, SUM(`Literate_Male`) AS Total_Literate_Males, SUM(`Literate_Female`) AS Total_Literate_Females, SUM(`Population`) AS Total_Population
FROM census_filtered GROUP BY `State/UT`;"""
cursor.execute(query_1)
result_1 = cursor.fetchall()
cursor.execute(query_2)
result_2 = cursor.fetchall()
cursor.execute(query_3)
result_3 = cursor.fetchall()
cursor.execute(query_4)
result_4 = cursor.fetchall()
cursor.execute(query_5)
result_5 = cursor.fetchall()
cursor.execute(query_6)
result_6 = cursor.fetchall()
cursor.execute(query_7)
result_7 = cursor.fetchall()
cursor.execute(query_8)
result_8 = cursor.fetchall()
cursor.execute(query_9)
result_9 = cursor.fetchall()
cursor.execute(query_10)
result_10 = cursor.fetchall()
cursor.execute(query_11)
result_11 = cursor.fetchall()
cursor.execute(query_12)
result_12 = cursor.fetchall()
cursor.execute(query_13)
result_13 = cursor.fetchall()
cursor.execute(query_14)
result_14 = cursor.fetchall()
cursor.execute(query_15)
result_15 = cursor.fetchall()
cursor.execute(query_literacy_rate)
result_literacy_rate = cursor.fetchall()
# Create a DataFrame for display
df_population = pd.DataFrame(result_1, columns=["District", "Total_Population"])
df_literacy = pd.DataFrame(result_2, columns=["District", "Total_Literate_Males", "Total_Literate_Females"])
df_workers = pd.DataFrame(result_3, columns=["District", "Total_Workers", "Total_Population", "Worker_Percentage"])
df_lpg_png = pd.DataFrame(result_4, columns=["District", "Households_with_LPG_or_PNG"])
df_religion = pd.DataFrame(result_5, columns=["District", "Total_Hindus", "Total_Muslims", "Total_Christians", "Total_Other_Religions"])
df_internet = pd.DataFrame(result_6, columns=["District", "Total_Internet_Access_Households"])
df_education = pd.DataFrame(result_7, columns=["District","Below_Primary_Total", "Primary_Total","Middle_Total","Secondary_Total","Higher_Total","Graduate_Total","Other_Total"])
df_assets = pd.DataFrame(result_8, columns=["District", "Bicycle_Households", "Car_Households", "Radio_Households", "Television_Households"])
df_house_conditions = pd.DataFrame(result_9, columns=["District", "Dilapidated_Houses", "Separate_Kitchen_Houses", "Bathing_Facility_Houses", "Latrine_Facility_Houses"])
df_total_households = pd.DataFrame(result_10, columns=["State/UT", "Total_Households"])
df_latrine_facility = pd.DataFrame(result_11, columns=["State/UT", "Total_Households_with_Latrine"])
df_avg_household_size = pd.DataFrame(result_12, columns=["State/UT", "Average_Household_Size"])
df_owned_rented = pd.DataFrame(result_13, columns=["State/UT", "Total_Owned_Households", "Total_Rented_Households"])
df_latrine_distribution = pd.DataFrame(result_14, columns=["State/UT","Total_Pit_Latrine", "Total_Other_Latrine"])
df_water_near_premises = pd.DataFrame(result_15, columns=["State/UT", "Households_Near_Drinking_Water"])
# Create a DataFrame for literacy data
df_literacy_rate = pd.DataFrame(result_literacy_rate, columns=["State/UT", "Total_Literate_Males", "Total_Literate_Females", "Total_Population"])
# Convert 'Total_Literate_Population' and 'Total_Population' columns to float
df_literacy_rate['Total_Literate_Population'] = df_literacy_rate['Total_Literate_Population'].astype(float)
df_literacy_rate['Total_Population'] = df_literacy_rate['Total_Population'].astype(float)
# Calculate Literacy Rate (%)
df_literacy_rate['Literacy_Rate (%)'] = (df_literacy_rate['Total_Literate_Population'] / df_literacy_rate['Total_Population']) * 100
st.write("### Total Population of Each District")
st.dataframe(df_population)
st.write("### Literate Male & Female Each District")
st.dataframe(df_literacy)
st.write("### Percentage of Workers (Male and Female) in Each District")
st.dataframe(df_workers)
st.write("### Households with LPG or PNG Access in Each District")
st.dataframe(df_lpg_png)
st.write("### Religious Composition of Each District")
st.dataframe(df_religion)
st.write("### Households with Internet Access in Each District")
st.dataframe(df_internet)
st.write("### Educational Attainment Distribution in Each District")
st.dataframe(df_education)
st.write("### Household Access to Assets by District")
st.dataframe(df_assets)
st.write("### Condition of Occupied Census Houses by District")
st.dataframe(df_house_conditions)
st.write("### Total Number of Households in Each State")
st.dataframe(df_total_households)
st.write("### Households with Latrine Facility within the Premises in Each State")
st.dataframe(df_latrine_facility)
st.write("### Average Household Size in Each State/UT")
st.dataframe(df_avg_household_size)
st.write("### Owned vs Rented Households in Each State/UT")
st.dataframe(df_owned_rented)
st.write("### Distribution of Latrine Facilities in Each State/UT")
st.dataframe(df_latrine_distribution)
st.write("### Households with Access to Drinking Water Near Premises in Each State")
st.dataframe(df_water_near_premises)
# Displaying the literacy rate in Streamlit
st.write("### Overall Literacy Rate (Percentage) in Each State/UT")
st.dataframe(df_literacy_rate[['State/UT', 'Literacy_Rate (%)']])
# Close the connection
cursor.close()
conn.close()    