#Chpt 19
#File Input and Output

#19.1 Opening Files
#use builtin 'open' function to open files, the open function can take many arguements as seen bellow
open(filename, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
# use 'r' in front of strings showing windows file paths to prevent errors or confusion due to the use of the '\'

a_file = open(r'C:\Users\justi\AppData\Local\Temp') # python creates this file in the directory, or overwrites a file if it already exists.


#19.2 Reading Text Files
passwd_file = open('/etc/passwd')
passwd_file.readline() #returns 1 line of the hypothetical file
print(passwd_file.read()) #reads all contents of the hypothetical file
passwd_file.close() #closes file, always do this when done with a file, dont forget to close it!

#19.3 Reading Binary Files
bfin = open('img/dict.png', 'rb') #pass in rb as mode to read binary files
bfin.read(8) #set to read 8 bytes

#19.4 Iteration With Files
fin = open('/etc/passwd')
for line in fin.readlines():
    print(line) #prints each line of the file at a time
#OR
for line in fin:
    print(line) #better then above method as it is not memory limited. Only use readlines() iteration if you know you
    #have enough memory or need to access a line multiple times


#19.5 Writing Files
fout = open('/tmp/names.txt', 'w') #to write to a file use 'w' mode
fout.write('George') #creates a file and adds string 'George' to it, if the file already exists, it overwrites it

#19.6 Closing Files
#use .close to close files
#you can also use 'with', to open execute and then close a file like so:
with open('/tmp/names3.txt', 'w') as fout3:
    fout.write('Ringo\r\n')
#which is the equivalent of:
fout3 = open('/tmp/names3.txt', 'w')
fout3.write('Ringo\r\n')
fout3.close()


#19.7 Designing around files
def add_numbers(filename):
    results = []
    with open(filename) as fin:
        for num, line in enumerate(fin):
            results.append('{0}-{1}'.format(num, line))
    return results
#refactored as two functions, easier to test and reuse, doesnt depend on a filename
def add_numbers(filename):
    with open(filename) as fin:
        return add_nums_to_seq(fin)

def add_nums_to_seq(seq):
    results = []
    for num, line in enumerate(seq):
        results.append('{0}-{1}'.format(num, line))
        return results