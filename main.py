# 🚨 Don't change the code below 👇
# age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#Welcome
print('Here you can know how many years your left to die!')

#Input and int convertion
age = int(input('¿What is your age? \n'))

#Operation to convert into days
#Calculated with 77 years as the hope life in Colombia on 2020
days_left = 77 - age 
p_days = days_left * 365

#Operation to convert into weeks
weeks_left = 77 - age
p_weeks = weeks_left * 53

#Operation to convert into months 
months_left = 77 - age
p_months = months_left * 12

#Result 
result = f'You left {p_days} days, {p_weeks} weeks and, {p_months} before die'
print(result)









