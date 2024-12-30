import pandas as pd
#File Path
file_path = r"census_2011_renamed.csv"
output_path = r"census_2011_state_ut_renamed.csv" #Output file for task 2
#Load the dataset
census_data = pd.read_csv(file_path)
#Defining the function to rename State/UT names
def rename_state_ut(name):
    words = name.split()
    formatted_words = []
    for word in words:
        if word.lower() == "and" :  #If the word is and
            formatted_words.append("and") #Keep it lowercase
        else:
            formatted_words.append(word.capitalize())  #Capitalize first letter
    return " ".join(formatted_words)
#Apply the function to State/UT columns
census_data["State/UT"] = census_data["State/UT"].apply(rename_state_ut)
#Saving the updated dataset 
census_data.to_csv(output_path, index=False)
print("State/UT names have been renamed successfully!")
print(census_data["State/UT"].head)