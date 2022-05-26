# Chp 18 Indexing and Slicing pg 129

#Indexing
my_pets = ['dog', 'cat', 'bird']
my_pets[0] #returns 'dog'
my_pets[-1] #returns 'bird'

#index on tuple
('Fred', 23, 'Senior')[1] #returns 23

#Index on string
'Fred'[0] #returns 'F'


#18.2 Slicing sub lists
my_pets = ['dog', 'cat', 'bird']
print(my_pets[0:2]) #prints ['dog','cat'] #Pyhon counts up to, but does not include,  the second index
print(my_pets[:2]) #prints ['dog, 'cat] #first index is optional, if it is omitted, default starts at 0
my_pets[0:-1]#['dog', 'cat']
my_pets[:-1] #['dog','cat']
my_pets[0:-2]#['dog']
#The final index is also optional, if it is omitted, the default is until the end of the list
my_pets[1:] #['cat','bird']
my_pets[-2:]#['cat', 'bird']
#if both indices are excluded, the entire list is returned as a copy of itself
print(my_pets[:]) #['dog','cat','bird']


#18.3 Striding Slices
#stride is an optional 3rd arguement, it's default is 1. it skips numbers based on input, ie. '2' is every other item
#'3' is every third item etc..
my_pets = ['dog','cat','bird']
dog_and_bird = my_pets[0:3:2]
print(dog_and_bird) #['dog','bird']

zero_three_six = [0, 1, 2, 3, 4, 5, 6][::3] #counts every third number
print(zero_three_six) #[0, 3, 6]

#negative strides
#Tip: make sure start slice is greater than end slice, unless both slices are omitted entirely
#stride of -1 reverses the list
my_pets[0:2:-1] # []
my_pets[2:0:-1] #['bird', 'cat']
print([1, 2, 3, 4][::-1]) #[4,3,2,1]
'emerih'[::-1] #'hireme'
