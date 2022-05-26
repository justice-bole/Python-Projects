#endswith
xl = 'Oct2000.xls'
xl.endswith('.xls')

#find
word = 'grateful'
print(word.find('ate'))
print(word.find('great'))

#format
print('name: {}, age: {}'.\
    format('Matt', 10))

#join
print(', '.join(['1','2','3']))

#lower
#okay
fname = 'readme.txt'
print(fname.endswith('txt') or fname.endswith('TXT'))

#Better
print(fname.lower().endswith('txt'))

#startswith
print('Book'.startswith('B'))
print('Book'.startswith('b'))

#.strip .lstrip .rstrip
print(' hello there '.strip())

#upper
print('yell'.upper())

#Excercises
#1
school = "mason"
correct_school = school.capitalize()
print(correct_school)

#2
country = "usa"
correct_country = country.upper()
print(correct_country)

#3
filename = "hello.py"
print(filename.endswith(".java"))
print(filename.find("py"))
print(filename.startswith("world"))