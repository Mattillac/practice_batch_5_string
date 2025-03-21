#Prog07: Create a program that ask the user to input a complete statement. Print the number of words in the input.
#input statement
your_statement = str(input("Enter your statement: "))
#imagine "Hi i like eating cookies, but sometimes i eat cake"
words_said = your_statement.split()
#expected output: 11
word_count = len(words_said)
#print number of words used in the statement
print("Words used:",word_count)