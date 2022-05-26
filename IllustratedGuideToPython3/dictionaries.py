#literal dictionary assignment
info = {'first': 'Pete', 'last': 'Best'}

#using built in dict class
info = dict([('first', 'Pete'),
             ('last', 'Best')])

#named parameters
info = dict(first='Pete', last='Best')

#using index operations to insert value into dictionary
info['age'] = 20
info['occupation'] = 'Drummer'

#retrieving values from a dictionary
info['age']
#returns 20

#the in operator
'Band' in info
#returns False
'first' in info
#returns True

#can use the in statement with a list, set, or string to check membership
5 in [1, 2, 6]
#returns False
't' in {'a', 'e', 'i'}
#returns False
'P' in 'Paul'
#returns True

#dictionary shortcuts using the .get method
genre = info.get('Genre', 'Rock')
#.get gets the value of a key, optional param 'Rock' sets 'Rock' to default value
# if key is not found
genre
#returns 'Rock'

# .setdefault method, used as a counter for a key, works like .get but can be mutated
names = ['Ringo', 'Paul', 'John', 'Ringo']
count = {}
for name in names:
    count.setdefault(name, 0)
    count[name] += 1
#without .setdefault
names = ['Ringo', 'Paul', 'John', 'Ringo']
count = {}
for name in names:
    if name not in count:
        count[name] = 1
    else:
        count[name] += 1
count['Ringo']
#returns 2
#using collections.Counter class
import collections
count = collections.Counter(['Ringo', 'Paul', 'John', 'Ringo'])
count
#returns Counter({'Ringo': 2, 'Paul': 1, 'John': 1})
count['Ringo']
#returns 2
count['Fred']
#returns 0

#Deleting keys using del statement
#remove 'Ringo' from dictionary
#Note: You cannot add or remove from a dictionary whilst it is looping over, it will throw an error
del names_to_bands['Ringo']

#Dictionary iteration
#can iterate over dictionary using 'for' keyword. by default returns keys
data = {'Adamn': 2, 'Zeek': 5, 'Fred': 3}
for name in data:
    print(name)
#returns
#Adam
#Zeek
#Fred
#To iterate over the values of a dictionary use the .values method
for value in data.values():
    print(value)
#returns
#2
#5
#3
#to get both key and value during iteration use the .items method
for key, value in data.items():
    print(key, value)
#returns
#Adam 2
#Zeek 5
#Fred 3
#if you turn the viw into a list, youll see that the list is a sequence of tuples
list(data.items())
#retuns [('Adam, 2), ('Zeek', 5), ('Fred', 3)]
#Note: Remember dict is ordered based on key insert order. If you want a diff order, use 'sorted'
for name in sorted(data.keys()):
    print(name)
#returns
#Adam
#Fred
#Zeek
#optional arg 'reverse' can be used to reverse order
for name in sorted(data.keys(),reverse=True):
    print(name)
#returns
#Zeek
#Fred
#Adam

#Merging Dictionaries using the dict unpacking operator '**'
color = {'phone': 'black', 'pen': 'yellow'}
color2 = {'car': 'red', 'pen': 'blue'}
{**color, **color2}
#returns: {'phone': 'black', 'pen': 'blue', 'car': 'red'}
#Using the .update method, mutates existing dict, doesnt return a new one
color.update(color2)
color2
#returns: {'phone': 'black', 'pen': 'blue', 'car': 'red'}
#using dict union '|'
color = {'phone': 'black', 'pen': 'yellow'}
color2 = {'car': 'red', 'pen': 'blue'}
color | color2 #last key overwrites first key
#returns: {'phone': 'black', 'pen': 'blue', 'car': 'red'}

