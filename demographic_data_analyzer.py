import pandas as pd

# input of function: "print_data=True"

def calculate_demographic_data():
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # Data cleaning
    df.dropna()
    df.drop_duplicates()

    # Race Count
    race_count = df.race.value_counts()

    # Average age of men
    men_in_df = df[df.sex == "Male"]
    average_age_men = round(men_in_df.age.mean(), 2)

    # Percentage of people w/bachelors degrees
    bachelors_count = len(df[df.education == "Bachelors"])
    percentage_bachelors = round((bachelors_count/ len(df)) * 100, 2)

    # Percentage of people with higher education who earn more than 50K a year:
    higher_education = df[(df.education == "Bachelors") | (df.education == "Masters") | 
                          (df.education == "Doctorate")]
    rich_higher_ed = higher_education[higher_education.salary == ">50K"]

    higher_education_rich = round((len(rich_higher_ed) / len(higher_education)) * 100, 2)

    # Percentage of people without higher education who earn more than 50K a year:
    lower_education = df[(df.education != "Bachelors") | (df.education != "Masters") | 
                         (df.education != "Doctorate")]
    rich_lower_ed = lower_education[lower_education.salary == ">50K"]

    lower_education_rich = round((len(rich_lower_ed) / len(lower_education)) * 100, 2)

    # Minimum number of hours a person works per week
    min_work_hours = df["hours-per-week"].min()

    # Percentage of the people who work the minimum number of hours per week who 
    # have a salary of >50K
    min_work = df[df["hours-per-week"] == min_work_hours]
    rich_min_work = min_work[min_work.salary == ">50K"]

    rich_percentage = round((len(rich_min_work) / len(min_work)) * 100, 2)

    # TODO What country has the highest percentage of people that earn >50K and what 
    # is that percentage?
    people_per_country = df["native-country"].value_counts()
    rich_people_total = df[df.salary == ">50K"]
    rich_ppc = rich_people_total["native-country"].value_counts()
    percentage_rich_ppc = round((rich_ppc/people_per_country) * 100, 2)

    highest_earning_country_percentage = percentage_rich_ppc.sort_values(ascending=False)[:1]
    print(highest_earning_country_percentage)
#
#    # TODO Identify the most popular occupation for those who earn >50K in India.
#    top_IN_occupation = None
#
#    # DO NOT MODIFY BELOW THIS LINE
#
#    if print_data:
#        print("Number of each race:\n", race_count) 
#        print("Average age of men:", average_age_men)
#        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
#        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
#        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
#        print(f"Min work time: {min_work_hours} hours/week")
#        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
#        print("Country with highest percentage of rich:", highest_earning_country)
#        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
#        print("Top occupations in India:", top_IN_occupation)
#
#    return {
#        'race_count': race_count,
#        'average_age_men': average_age_men,
#        'percentage_bachelors': percentage_bachelors,
#        'higher_education_rich': higher_education_rich,
#        'lower_education_rich': lower_education_rich,
#        'min_work_hours': min_work_hours,
#        'rich_percentage': rich_percentage,
#        'highest_earning_country': highest_earning_country,
#        'highest_earning_country_percentage':
#        highest_earning_country_percentage,
#        'top_IN_occupation': top_IN_occupation
#    }
#

calculate_demographic_data()