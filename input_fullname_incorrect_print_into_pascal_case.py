#Prog09: Create a program that ask the user to input their fullname in incorrect casing. Print the input in pascal case.
#input name
name = str(input("Enter your name: "))
#imagine tObias fOXtROT
pascal_cased = name.title().replace(" ","")
#print TobiasFoxtrot
print("Your name in Pascal Case:",pascal_cased)