'''

Create get_generation function
Accepts no parameters
Returns a string with the name of the generation
Generation	Start Year	End Year
Alpha	        2013	2025
Gen Z	        1997	2012
Millennial	    1981	1996
Gen X	        1965	1980
Baby Boomer	    1946	1964
Wow!	     All else	All else
Call the function and print the return value three times

resources: 
https://www.w3schools.com/python/python_operators.asp
https://www.w3schools.com/python/python_conditions.asp
https://www.w3schools.com/python/python_functions.asp
https://stackoverflow.com/questions/13628791/determine-whether-integer-is-between-two-other-integers#:~:text=While%2010%20%3C%3D%20number%20%3C%3D,%22outside%20of%20range!%22)





'''

def get_generation(birth_year):
    if birth_year in range(1946, 1964):
        print(f"You are a Baby Booomer!")
    elif birth_year in range (1965, 1980):
        print(f"You are a Gen X")
    elif birth_year in range (1981, 1996):
        print("you are a Millennial")
    elif birth_year in range(1997, 2017):
        print("You are Gen Z")
    elif birth_year in range (2013, 2025):
        print("you are Alpha")
    elif birth_year < 1964:
        print("Woow!")

birth_year = int(input("Enter your birth year: "))
get_generation(birth_year)
