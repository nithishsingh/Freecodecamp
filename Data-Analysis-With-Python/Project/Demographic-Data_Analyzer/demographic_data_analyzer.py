import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df[df['education'] == 'Bachelors'].shape[0] / df.shape[0]) * 100, 1)

    # Series of people with a higher education
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # Series of people without a higher education
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    higher_education_rich = round((higher_education[higher_education['salary'] == '>50K'].shape[0] / higher_education.shape[0]) * 100, 1)

    # What percentage of people without advanced education make more than 50K?
    lower_education_rich = round((lower_education[lower_education['salary'] == '>50K'].shape[0] / lower_education.shape[0]) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # Series of people who work the min number of hours / week
    num_min_workers = df[df['hours-per-week'] == min_work_hours]

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    rich_percentage = round((num_min_workers[num_min_workers['salary'] == '>50K'].shape[0] / num_min_workers.shape[0]) * 100, 1)

    # Multi Index series containing the number of people with a salary >50K in each country ([native-country, salary, #])
    num_ppl_sal = df[df['salary'] == '>50K'].groupby('native-country')['salary'].value_counts()

    # Series containing the total number of people in each country ([native-country, #])
    num_ppl_tot = df.groupby('native-country').size()

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = (num_ppl_sal / num_ppl_tot * 100).idxmax()[0]

    # What is that percentage?
    highest_earning_country_percentage = round((num_ppl_sal / num_ppl_tot * 100).max(), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    gt_50 = df[df['salary'] == '>50K']
    top_IN_occupation = gt_50[gt_50['native-country'] == highest_earning_country]['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
