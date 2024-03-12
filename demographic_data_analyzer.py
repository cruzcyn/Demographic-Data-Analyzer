import pandas as pd

# input of function: "print_data=True"

def calculate_demographic_data():
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    race_count = df.race.value_counts()

#    # TODO What is the average age of men?
    men_in_df = df[df.sex == "Male"]
    average_age_men = round(men_in_df.age.mean(), 2)
    print(average_age_men)
#
#    # TODO What is the percentage of people who have a Bachelor's degree?
#    percentage_bachelors = None
#
#    # TODO What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) 
     # make more than 50K?
    
#    # TODO What percentage of people without advanced education make more than 50K?
#
#    ## with and without `Bachelors`, `Masters`, or `Doctorate`
#    higher_education = None
#    lower_education = None
#
#    ##  percentage with salary >50K
#    higher_education_rich = None
#    lower_education_rich = None
#
#    # TODO What is the minimum number of hours a person works per week (hours-per-week feature)?
#    min_work_hours = None
#
#    # TODO What percentage of the people who work the minimum number of hours per week have a salary of >50K?
#    num_min_workers = None
#
#    rich_percentage = None
#
#    # TODO What country has the highest percentage of people that earn >50K and what is that percentage?
#    highest_earning_country = None
#    highest_earning_country_percentage = None
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