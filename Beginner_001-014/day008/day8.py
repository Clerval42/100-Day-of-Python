""" def function():
    print("a string")
function()

def f_with_input(strings):
    print(f"string with {strings}")
f_with_input("dsaf")
 """



""" # Write your code below this line 👇
import math
def paint_calc(height, width, cover):
    number_of_can = math.ceil((height*width)/cover)
    print(f"You'll need {number_of_can} cans of paint.")
# Write your code above this line 👆
# Define a function called paint_calc() so the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage) """




# Write your code below this line 👇
def prime_checker(number):
    isPrime = True
    i = 2
    while isPrime:
        if n%i-- == 0:
            isPrime = False
    if isPrime == True:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")



# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)