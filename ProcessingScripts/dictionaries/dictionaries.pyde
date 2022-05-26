student = ['Sam', 24]
student = {'name': 'Sam', 'age': 24}

print(student['age'])
print(student['name'])

student['age'] = 25

student['id'] = 19950501

del student['age']

print(student)

students = { #dictionary with lists
            'names': ['Sam','Lee'],
            'ids': ['19950501','19991114']
            }
print(students['names'][1])

students = [ #list with dictionaries
            {'name':'Sam','id': 19950501},
            {'name':'Lee', 'id': 19991114}
            ]
print(students[1]['name'])

courses = {
           'game development' : 'Prof. Smith',
           'web design' : 'Prof. Ncube',
           'code art' : 'Prof. Sato'
           }

for course in sorted(courses):  #for keys #can't rely on dictionary to be sorted or in order without sorted()
    print(course)

print(sorted(courses.keys())) # if you just need a list of the keys

for prof in courses.values(): #for values and not keys
    print(prof)
    
print(courses.items()) # prints keys and values

for kv in courses.items():
    print(kv)
    
#for course, prof in sorted(courses.items()):
for course, prof in reversed(sorted(courses.items())): # sorted is always based on key value
    print('{} coordinates {} course.'.format(prof, course))
