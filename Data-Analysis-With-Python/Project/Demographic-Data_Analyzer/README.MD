# Demographic Data Analysis

This repository contains a Python script for analyzing demographic data using Python and Pandas.

## Usage

1. Clone the repository or download the files to your local machine.
2. Ensure you have Python installed.
3. Install the necessary dependencies:

    ```bash
    pip install pandas
    ```

4. Run the `main.py` script to test the `calculate_demographic_data` function:

    ```bash
    python main.py
    ```

## Demographic Data Analysis

The `calculate_demographic_data` Python script performs demographic analysis on a dataset containing information about individuals. The analysis includes computations related to race representation, education levels, salaries, and more.

### Function Details

The `calculate_demographic_data` function conducts the following tasks:

- Reads the dataset file `adult.data.csv`.
- Analyzes demographic data, such as race representation, education levels, average age of men, minimum work hours, and percentages across various demographics.
- Identifies the country with the highest percentage of individuals earning over 50K.
- Determines the most popular occupation among individuals earning over 50K in India.

### Output

The function returns a dictionary containing the following demographic data:

- `race_count`: Number of individuals from each race.
- `average_age_men`: Average age of men.
- `percentage_bachelors`: Percentage of individuals with a Bachelor's degree.
- `higher_education_rich`: Percentage of individuals with advanced education earning over 50K.
- `lower_education_rich`: Percentage of individuals without advanced education earning over 50K.
- `min_work_hours`: Minimum number of work hours per week.
- `rich_percentage`: Percentage of individuals earning over 50K among those working the minimum hours.
- `highest_earning_country`: Country with the highest percentage of individuals earning over 50K.
- `highest_earning_country_percentage`: Highest percentage of individuals earning over 50K in a country.
- `top_IN_occupation`: Most popular occupation among individuals earning over 50K in India.

### Note

Ensure the dataset file `adult.data.csv` is correctly formatted and placed in the script's directory before running the analysis.
