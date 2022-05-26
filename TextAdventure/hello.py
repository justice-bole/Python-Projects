# This program says "hello" and asks for the user's name and age.

print('Hello, friend!')     #greeting
print('What is your name?')     #asks for name
myName = input()       #get name
print('It is a good to meet you, ' + myName)    #says name
print('The length of your name is:')    #gives name character length
print(len(myName))
print('What is your age?') #ask for their age
myAge = input()     #get age
print('You will be ' + str(int(myAge) + 1) + ' in a year.')     #says next years age
