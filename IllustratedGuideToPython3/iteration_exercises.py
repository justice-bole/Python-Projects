#1 create a list of names, calc the avg length of names
friends_list = ["Justice", "Jake", "Mary", "Sage", "Stacie", "Piper"]
name_length = 0
for names in friends_list:
    name_length += len(names)
    avg_name_length = name_length / len(friends_list)
print(avg_name_length) #COMPLETE!


#2 create a list of names, search for name John using for loop, print 'not found' if name is not found.
name_list = ['Justice', 'Breanna', 'Mary', 'Sage', 'Garrett', 'Justin', 'Steve', 'John']
name = 'John'
is_present = False
for names in name_list:
    if name in names:
        is_present = True
        break
    else:
        is_present = False
if is_present:
    print("Found " + name + "!")
else:
    print(name, 'was not found!')


#3 create a list of tuples of first names, last names, and ages. Use 'none' for ages you don't know. Calc avg age,
# skipping 'none' values. Print each name, followed by 'old' or 'young' if they are above or below the avg age
age_list = [('Justice', 'Bole', 27), ('Mary', 'Keim', 26), ('Sage', 'Bole', 'None'), ('Diana', 'Bole', 78)]
total_age = 0
for tuples in age_list:
    if 'None' in tuples:
        continue
    age = tuples[2]
    total_age += age

avg_age = total_age / len(tuples)

for tuples in age_list:
    if 'None' in tuples:
        continue
    if tuples[2] < avg_age:
        print(tuples[0], tuples[1], 'young')
    else:
        print(tuples[0], tuples[1], 'old')

