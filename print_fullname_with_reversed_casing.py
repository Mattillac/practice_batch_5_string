#Prog06: Create a program that ask the user to input their fullname in incorrect casing. Print each character of the input in reverse casing.
#input name
name = str(input("Enter your name: "))
#imagine tObias fOXtROT
reversed_cased = name.swapcase()
#print tOBIAS fOXTROT
print("Your name in esrever gnisac:",reversed_cased)