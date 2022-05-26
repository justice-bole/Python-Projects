for letter in ['c', 'a', 't']:
    print(letter)

#smells bad
animals = ["cat", "dog", "bird"]
for index in range(len(animals)):
    print(index, animals[index])

#smells good
animals = ["cat", "dog", "bird"]
for index, value in enumerate(animals):
    print(index, value)

# break example
numbers = [3, 5, 9, -1, 3, 1]
result = 0
for item in numbers:
    if item in numbers:
        if item < 0:
            break
        result += item
print(result)

#continue or skip example
numbers = [3, 5, 9, -1, 3, 1]
result = 0
for item in numbers:
    if item < 0:
        continue
    result += item
print(result)

#in statement can  be used for membership
animals = ["cat", "dog", "bird"]
'bird' in animals
#returns true
#if you want the index location
animals.index('bird')
#returns 2

#remove item fron list #method 1
names = ['John', 'Paul', 'George', 'Ringo']
names_to_remove = []
for name in names:
    if name not in ['John', 'Paul']:
        names_to_remove.append(name)
for name in names_to_remove:
    names.remove(name)
print(names)

#remove item from list #method 2 (slice copy contruct)
names = ['John', 'Paul', 'George', 'Ringo']
for name in names[:]: # copy of names
    if name not in ['John', 'Paul']:
        names.remove(name)
print(names)

#else clauses
items = [1, 2, 3, -1, 0]
positive = False
for num in items:
    if num < 0:
        break
else:
    positive = True

# While loops
n = 3
while True:
    print(n)
    n -= 1
    if n == 0:
        break

#walrus operator, b4 and after
#b4
done = False
while not done:
    items = result.fetchmany(count)
    done = len(items) == 0
    if not done:
        for item in items:
            process(item)
#after
while len(items := result.fetchmany(count)) != 0:
    for item in items:
        process(item)
#b4
txt = input('> ')
while txt == '':
    print("please type something")
    txt = input('> ')
#after
while (txt:= input('> ')) == '':
    print("please type something")

