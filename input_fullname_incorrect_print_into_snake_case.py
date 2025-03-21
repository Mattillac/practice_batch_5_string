#Prog10: Create a program that ask the user to input their fullname in incorrect casing. Print the input in snake case.
#input name
name = str(input("Enter your name: "))
#iamgine KiNg koNg
snake_cased = name.lower().replace(" ","_")
#prints king_kong
print("Your name in snake case:",snake_cased)