'''
Create a calc_change function that does the following:
Accepts one parameter representing an amount of money
Calculate and output the least amount of change using the 
following denominations: 
Dollar (100 cents), Quarter (25 cents), Dime (10 cents), 
Nickel (5 cents), Penny (1 cent)
if a denomination is not used, do not display it
Call the calc_change function with the appropriate argument 
from the user


**notes**
bool values are T or F
True and False are boolean literal 

-Conditional expressions:
    statement that resolves to a value of True or False

-Comparison Operators: 
    Anytime we see a comparison operator,the result is a Boolean Value
    math operators
    > 
    >=
    <
    <=
    ==
    !=

Logical operators:
    evaluete conditional expressions. anytime we see a logical operator, the result is a boolean value 
    three logical operators
        and- both must be true 
        or-  either or one operand must be true
        not- flips a boolean alue 

'''

#examples
from math import remainder
from shelve import DbfilenameShelf


test_one = 5 < 6  
print(test_one)
print(5 > 6)
print(5 == 6)
print(5 != 6)


#function for calc_change testing 2.98
def calc_change(money):
    dollar = money//1
    money = money % 1

    quarters = money // .25
    money = round(money % .25, 2)

    dimes = money // .10
    money = round(money % .10, 2)

    nickels = money // .05
    money = round(money % .05, 2)

    pennies = money / .01
    
    if dollar > 0:
        print(f'{int(dollar)} dollar(s)')
    if quarters > 0:
        print(f'{int(quarters)} Quarter(s)')
    if dimes > 0:
        print(f'{int(dimes)} dime(s)')
    if nickels > 0:
        print(f'{int(nickels)} nickel(s)')
    if pennies > 0:
        print(f'{int(pennies)} penny(ies)')

money = float(input("Enter an amount: "))
calc_change(money)
