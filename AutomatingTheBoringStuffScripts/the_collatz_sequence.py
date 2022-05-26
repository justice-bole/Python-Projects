def collatz(number):
    if number % 2 == 0:
        number = number // 2
        return number
    else:
        number = 3 * number + 1
        return number

try:
    user_number = int(input('Enter an integer: \n'))
except:
    print('Error: Invalid Input, please use only whole number integers.')

while user_number != 1:
    user_number = collatz(user_number)
    print(user_number)









