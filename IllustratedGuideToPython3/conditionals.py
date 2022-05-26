number = 4
modulo4 = number % 4
modulo400 = number % 400
modulo100 = number % 100

if modulo400 == 0:
    print(number, "is a leap year!")
elif modulo4 == 0 and modulo100 != 0:
    print(number, "is a leap year!")
else:
    print(number, "is not a leap year.")

new_number = 3
even_odd = new_number % 2

if even_odd == 0:
    print(new_number, "is even.")
else:
    print(new_number, "is odd.")