'''

Import date from datetime
Create a get_birthdate function
Accepts no parameters
Gets year, month, and day from the user
Returns a date object based on the input
Create a get_age function
Accepts one parameter of a date object
Compares the parameter against todays date and converts th
e detlatime into an integer representing the age
Returns the age
Call the correct functions to get the users age and output the following
Is the user old enough to drive, vote, and be president
If the user is old enough to be president, first ask if they are a 
natural born citizen
If the user is a natural born citizen, then ask if they have been a 
US resident for 14 years
If they have, inform them they can run for president
Inform the user if they are not middle aged (not between 35 and 60)

resources: 
https://www.w3schools.com/python/python_datetime.asp


'''
from datetime import date

def get_bdate():
    year = int(input("Enter your birth year: "))
    month = int(input("Enter your birth month: "))
    day = int(input("Enter your birth day: "))
    return date(year, month, day)

def get_age(date):
    today = date.today()
    age = today - date
    return age.days //365.25

user_age = get_age(get_bdate())

if user_age > 15:
    print("You can drive")
if user_age > 17: 
    print("You can vote")
if user_age > 34:
    if input("Are  you a natural born citizen (y/n): ") == "y":
        if input("Have you lived in the US for 14 years? (y/n): ") == "y":
            print("You can be president")
if user_age not in range(35, 60):
    print("you are not Middle aged.")