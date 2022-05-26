#17.7 Function Exercises pg. 118

# 1 write a func, is_odd, that takes an int and returns true if odd, false if not.
def is_odd(num):
    """returns even or odd based on number"""
    if num % 2 == 1:
        print('odd')
        return True
    else:
        print('even')
        return False
is_odd(3)
is_odd(6)

# 2 write a func, is_prime, that takes an int and returns True if the no. is prime, and False if not.
def is_prime(number):
    """returns true for prime numbers, false if not"""
    if number <= 1.0:
        return False
    if number != 2.0 and number % 2.0 != 1.0:
        return False
    i = 1
    while i < number:
        result = number / i
        i += 1
        if result != number and result % 2 in [0, 1]:
            return False
        else:
            return True
print(is_prime(11.0))

# 3 write a binary search function that takes a sorted sequence, and item it is looking for, return index of item if
# found, -1 if not found
def find_index(seq, item):
    print(seq.index(item))

find_index(["apple", "banana", "cherry"], "apple")

# 4 write a func that takes camelCase strings and converts them to snake_case, add optional arg, seperator so it will
# also convert to kebab-case
def snake_converter(camel, default=None):
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for letter in camel:
        if letter in alphabet:
            letter.replace(letter,"_")
    camel = camel.lower()
    print(camel)
snake_converter('helloWorld')
#NOT FINISHED



