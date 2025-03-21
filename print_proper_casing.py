#Prog05: Create a program that ask the user to input their fullname in incorrect casing. Print the input in proper casing.
#input name
name = str(input("Enter your name: "))
#imagine tObias fOXtROT
proper_casing = name.title()
#print Tobias Foxtrot
print("Your name in proper casing:",proper_casing)