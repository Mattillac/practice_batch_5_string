#Prog01: Create a program that ask the user to input their fullname with several space characters at the beginning. Print the input without the spaces in the beginning
#input name with spaces
name = str(input("Enter your name with space: "))
#remove spaces
cutted_name = name.lstrip()
#print name without spaces 
print(cutted_name)
