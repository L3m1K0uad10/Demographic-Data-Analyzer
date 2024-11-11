import pandas as pd


def calculate_demographic_data(print_data=True):
    # Reading data from file
    df = pd.read_csv("adult.data.csv")


    # race are represented in this dataset This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()


    # the average age of men
    men_no = df["sex"].value_counts().iloc[0]
    query = (df["sex"] == " Male") | (df["sex"] == "Male") | (df["sex"] == "Male")

    average_age_men = round(df[query]["age"].mean(), 1)


    # the percentage of people who have a Bachelor's degree
    education_no = df["education"].value_counts().iloc[2]

    percentage_bachelors = round((education_no / df.shape[0]) * 100, 1)


    # percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K
    # percentage of people without advanced education make more than 50K
    df['salary'] = df['salary'].str.strip()
    query1 = (
        (df['education'] == 'Bachelors') |  
        (df['education'] == 'Masters') | 
        (df['education'] ==  'Doctorate')
    )
    query2 = (
        (df['education'] != 'Bachelors') &  
        (df['education'] != 'Masters') & 
        (df['education'] !=  'Doctorate')
    )
    query3 = (query1 & (df["salary"] == ">50K"))
    query4 = (query2 & (df["salary"] == ">50K"))

    total_higher_education = df[query1].shape[0]
    total_lower_education = df[query2].shape[0]

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[query3].shape[0]
    lower_education = df[query4].shape[0]

    # percentage with salary >50K
    higher_education_rich = round((higher_education / total_higher_education) * 100, 1)
    lower_education_rich =  round((lower_education / total_lower_education) * 100, 1)


    # the minimum number of hours a person works per week (hours-per-week feature)
    min_work_hours = df["hours-per-week"].unique().min()


    # percentage of the people who work the minimum number of hours per week have a salary of >50K
    num_rich_min_workers = df[
        (df["hours-per-week"] == min_work_hours) &
        (df["salary"] == ">50K")
    ].shape[0]   

    num_min_workers = df[df["hours-per-week"] == min_work_hours].shape[0]

    rich_percentage = round((num_rich_min_workers / num_min_workers) * 100, 1)


    # country has the highest percentage of people that earn >50K
    total_count_per_country = df["native-country"].value_counts()
    highest_earning_worker_countries = df[df["salary"] == ">50K"]["native-country"].value_counts()
    highest_earning_worker_countries_percentage = (highest_earning_worker_countries / total_count_per_country) * 100

    highest_earning_country = highest_earning_worker_countries_percentage.idxmax()
    highest_earning_country_percentage = round(highest_earning_worker_countries_percentage.max(), 1)


    # the most popular occupation for those who earn >50K in India.
    rich_indian_worker_occupation = df[(df["salary"] == ">50K") & (df["native-country"] == "India")]["occupation"].value_counts()

    top_IN_occupation = rich_indian_worker_occupation.idxmax()



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
