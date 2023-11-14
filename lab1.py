'''

Create a get_area function that does the following:
Accepts two parameters
Returns the area by multiply the two parameters
Create a calculate_area_from_user function that does the following:
Accepts no parameters
Gets two float inputs from the user
Calculates the area using the previous function
Prints the result rounded to the hundredths place
Run the calculate_area_from_user function three times


 ctr + / 

multiple parameteres are separated by comas
anything after the return statement will not run 
value in parenthesis of a function are arguments
'''


def get_area(lenght, widht):
    return lenght * widht

def calculate_area_from_user():
    lenght = float(input("Enter the lenght of the area: "))
    widht = float(input("Enter the widht of the area: "))
    area = get_area(lenght, widht)
    print(f"Area is:{area}")
#calculate_area_from_user()

#looping for in range for 3 runs in PY 
#https://www.w3schools.com/python/python_for_loops.asp
for x in range(3):
    calculate_area_from_user() 