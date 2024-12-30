# Census-Data-Standardization
# Census Data Standardization and Analysis Pipeline

This project is a part of the GUVI Data Engineering course, aimed at building a comprehensive pipeline for standardizing and analyzing census data. The project utilizes Python, pandas, SQL, MongoDB, and Streamlit to achieve the objectives. The main goal of this project is to clean, standardize, and analyze census data from the 2011 Census of India. This involves multiple steps such as data preprocessing, renaming columns, removing unnecessary columns, and uploading the processed data to a MySQL database. Additionally, data analysis and visualization are performed using Streamlit, providing insights into the census data.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Tasks Completed](#tasks-completed)
- [Future Enhancements](#future-enhancements)
- [License](#license)

## Overview
The Census Data Standardization and Analysis Pipeline is designed to:
- Clean and preprocess raw census data.
- Rename and standardize column headers.
- Integrate data into SQL databases for efficient querying.
- Visualize the processed data through Streamlit dashboards.

This pipeline simplifies working with large datasets and provides valuable insights from the census data.

## Features
- **Data Cleaning**: Remove unnecessary columns and standardize state/UT names.
- **SQL Integration**: Upload clean data to MySQL for structured queries.
- **Visualizations**: Create dashboards using Streamlit for data analysis.
- **Multi-Database Support**: MongoDB for initial storage and MySQL for final analysis.

## Tech Stack
- **Programming Language**: Python
- **Libraries**: pandas, numpy, mysql-connector-python, pymongo, Streamlit
- **Database**: MySQL, MongoDB
- **IDE**: Visual Studio Code
- **Version Control**: Git and GitHub

## Project Structure
```
|-- census_project
    |-- data/
    |   |-- census_raw.csv
    |   |-- census_2011_renamed.csv
    |-- scripts/
    |   |-- data_cleaning.py
    |   |-- upload_to_mysql.py
    |   |-- visualize_data.py
    |-- README.md
    |-- requirements.txt
```
- **data/**: Contains raw and processed datasets.
- **scripts/**: Python scripts for cleaning, uploading, and visualizing data.
- **README.md**: Documentation for the project.
- **requirements.txt**: Dependencies required for the project.

## Setup and Installation
### Prerequisites
- Python (3.8 or higher)
- MySQL Server
- MongoDB

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/census-project.git
   cd census-project
   ```
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up MySQL and MongoDB:
   - Create a MySQL database (e.g., `census_db`).
   - Update the database credentials in `upload_to_mysql.py`.
4. Run the scripts:
   - Clean the data:
     ```bash
     python scripts/data_cleaning.py
     ```
   - Upload data to MySQL:
     ```bash
     python scripts/upload_to_mysql.py
     ```
   - Launch the visualization dashboard:
     ```bash
     streamlit run scripts/visualize_data.py
     ```

## Usage
1. Preprocess raw census data using the `data_cleaning.py` script.
2. Upload the cleaned data to MySQL using the `upload_to_mysql.py` script.
3. Use the Streamlit dashboard for visualizing and analyzing the data.

## Tasks Completed
1. **Task 1**: Renamed columns in the dataset and saved as `census_2011_renamed.csv`.
2. **Task 2**: Standardized State/UT names.
3. **Task 3**: Removed unnecessary columns and verified data.
4. **Task 4**: Uploaded cleaned data to MySQL.
5. **Task 5**: Created a Streamlit dashboard for visualization.
6. **Task 6**: Save the processed data to mongoDB with a collection named “census” .
7. **Task 7**: Run Query on the database and show output on streamlit


## Future Enhancements
- Add more visualizations for in-depth analysis.
- Extend support for additional data formats.
- Automate the entire pipeline using Apache Airflow.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
