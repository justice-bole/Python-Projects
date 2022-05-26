#19.9 Exercises pg. 141-142
#File Input and Output

#1 Write a function to write a comma seperated value (CSV) file. It should accept a filename and a list of tuples as
#parameters. The tuples should have a name, address, and age. The file should create a header row followed by a row for
# each tuple.

information = [('George', '4312 Abbey Road', 22),
               ('John', '54 Love Ave', 21)]

def organize(info):
    results = []
    for line in info:
        print(line)


organize(information)