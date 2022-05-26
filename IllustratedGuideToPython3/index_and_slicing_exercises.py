#18.5 Index and Slicing Exercises pg. 133

#1 Create a var with name stored as a string. use index op to pull out the 1st char, then the last char, including names
# of arbitrary length.
my_name = 'Justice'
print(my_name[0])
print(my_name[-1])

#2 create a var. filename, assume it has a 3 letter extension, use slice to find the extension. Print the filename
# without the extension, must work with names of arbitrary length
filename = 'README.txt'
print(filename[-3:])
print(filename[:-4])

#3 create a function, is_palindrome, to determine is a word is the same if the letters are reversed
def is_palindrome(word):
    if word == word[::-1]:
        print(word.capitalize(), 'is a palindrome!')
    else:
        print(word.capitalize(), 'is not a palindrome.')

is_palindrome('racecar')
