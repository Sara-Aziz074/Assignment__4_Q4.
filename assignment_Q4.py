#Instructions: Implement Python programs to accomplish the following task

#Task

#You are tasked with creating a Python program that serves as an interactive
#  tool for a friend who enjoys exploring numbers. The program should begin 
# by prompting the user to enter their name and then ask them for three of 
# their favorite numbers.


#  After gathering this information, the program should
#  greet the user with a personalized message that includes their name. 


# The three numbers provided by the user should be stored in a list.
name = input("what is  your name? ") # Prompt the user to enter their name

print("what are three of your favorite numbers? ") # Ask for three of the user's favorite numbers

user_nmbr  = []  #empty list to store the favorite numbers
for i in range (3):

    inpt = int(input("Enter Your Favorite Numbers  : "))  # Prompt the user to enter each favorite number
    # user_nmbr.append(inpt)

  
# The program should then check if any of the numbers are even or odd,
#  and store this information in a separate list of tuples, where each tuple
#  contains the number and a string indicating whether it is "even" or "odd".

    if inpt  % 2 == 0 :
        user_nmbr.append((inpt,"even") )  # append tuple (number, "even") to the list.
    else:
        user_nmbr.append((inpt,"odd")) # append tuple (number, "odd") to the list.
    
      
# Greet the user with a personalized message including only the numbers (not "even"/"odd" info)
print(f"Hello, {name}! Let's explore your favorite numbers:")

# Display the even/odd status of each number
print("Here's whether each of your favorite numbers is even or odd:")
for numb, status in user_nmbr:
    print(f"The number: {numb} is {status}.")


#  Following this, the program should use a for loop to iterate over the list of 
# numbers, and for each number, it should create a tuple containing the number and 
# its square.
for numb, status in user_nmbr:
    square : int = numb **2
    print(f"The number: {numb} is {square}")
     

      
# 
#  These tuples should be printed in a creative and engaging format.
#  Additionally, the program should calculate the sum of the three numbers and
#  print the result, accompanied by an encouraging message.

totl_nbr :int = sum (num for num, _ in user_nmbr) # Calculate the sum of the numbers
print(f"Amazing! The sum of your favorite numbers is: {totl_nbr} ")
#  Finally, the program
#  should determine if the sum is a prime number and notify the user with an 
# appropriate message. The goal is to make the tool both enjoyable and informative,
#  allowing the user to explore their favorite numbers in a fun and interactive way,
#  while also introducing some interesting logical checks.

pri_nbr : int = totl_nbr

if pri_nbr == totl_nbr :
    print(f"Wow, {totl_nbr} is a prime number!")
    

