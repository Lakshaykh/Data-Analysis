#!/usr/bin/env python
# coding: utf-8


from ucimlrepo import fetch_ucirepo 
import pandas as pd
# fetch dataset 
adult = fetch_ucirepo(id=2) 
  
# data (as pandas dataframes) 
X = adult.data.features 
y = adult.data.targets 
  
# metadata 
print(adult.metadata) 
  
# variable information 
print(adult.variables) 
pd.DataFrame(X)
pd.DataFrame(y)

merged = pd.concat([X, y], axis=1)

pd.DataFrame(merged)
merged['income'] = merged['income'].replace({'<=50K.':'<=50K','>50K.':'>50K'})


# How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. (race column)
si=merged.groupby('race').size()
print(si)




# What is the average age of men?
av=merged[merged['sex']=='Male']['age'].mean()
print(av)


# What is the percentage of people who have a Bachelor's degree?
only=merged[merged['education']=='Bachelors'].shape[0]
total=merged['education'].shape[0]
percentage=(only/total)*100
print(percentage)

# What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?

advanced_education_high_income = merged[merged['education'].isin(['Bachelors', 'Masters', 'Doctorate']) & (merged['income'].isin(['>50K']))].shape[0]
total=merged[merged['education'].isin(['Bachelors', 'Masters', 'Doctorate'])].shape[0]
# Calculate the percentage
percentage_advanced_education_high_income = (advanced_education_high_income / total) * 100

print(f" {percentage_advanced_education_high_income:.2f}%")





# What percentage of people without advanced education make more than 50K?
without_advanced_education_high_income = merged[merged['education'].isin(['10th', '11th', '12th','1st-4th','5th-6th','7th-8th','9th']) & (merged['income'].isin(['>50K']))].shape[0]
total_less_education=merged[merged['education'].isin(['10th', '11th', '12th','1st-4th','5th-6th','7th-8th','9th'])].shape[0]
percentage=(without_advanced_education_high_income/total_less_education)*100
print(f" {percentage:.2f}%")



# What is the minimum number of hours a person works per week?
min_hours_per_week =merged['hours-per-week'].min()
print(f"The minimum number of hours a person works per week is: {min_hours_per_week}")



# What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
min_hours_per_week = merged['hours-per-week'].min()
min_hours_high_income = merged[(merged['hours-per-week'] == min_hours_per_week) & ((merged['income'] == '>50K') )]
# Calculate the percentage
total_min_hours = merged[merged['hours-per-week'] == min_hours_per_week].shape[0]
percentage_min_hours_high_income = (min_hours_high_income.shape[0] / total_min_hours) * 100
print(f"The percentage of people who work the minimum number of hours per week and have a salary of more than '50K' is: {percentage_min_hours_high_income:.2f}%")


# What country has the highest percentage of people that earn >50K and what is that percentage?
high_inc=merged[merged['income']==">50K"]
high_country_inc=high_inc.groupby('native-country').size()
perc=(high_country_inc/merged.groupby('native-country').size())*100
high_country=perc.idxmax()
high_perc=perc.max()
print(f"The country with the highest percentage of people earning >50K is {high_country} with a percentage of {high_perc:.2f}%.")


# Identify the most popular occupation for those who earn >50K in India.
only_india=merged[merged['native-country']=='India']
only_more_50k=only_india[only_india['income']=='>50K']
all_occ=only_more_50k.groupby('occupation').size()
occ_more_50k=all_occ.idxmax()
print(f"In india '{occ_more_50k}' earns more than 50 k")