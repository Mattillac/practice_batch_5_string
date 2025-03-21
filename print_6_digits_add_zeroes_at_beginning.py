#Prog02: Create a program that ask the user to input a number (0-1000). Print the number in 6 digit format. Add zeros at the beginning to complete the 6 digit.
#input number   
number = input("Enter a number: ")
#imagine inputted number is 123
formed_number = number.zfill(6)
#must print 000123  
print("Your entered number in a 6 digits form:",formed_number)