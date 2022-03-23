#! /usr/bin/env python3

"A module for finding particular words in a file"

# Importing modules
import re
import sys

# Defining regular expression to find words
regex = r'\w*herit\w*'

# Including uppercase and lowercase letters in searching the origin.txt file
darwin = re.compile(regex, re.IGNORECASE)

# Defining the function "find" 
def find():

    """
    Returns a file with some particular words.
    """
# Opening the yeshua file and writing the search results in find.txt which is the output file  
    print('Opening origin.txt')
    with open('origin.txt', 'r') as yeshua:
        with open('find.txt', 'w') as out:
            index = 0
    
# Formatting and adding line numbers to output file
            for line in yeshua:
                line = line.strip()
                list = line.split()
                index += 1
                find = darwin.search(line)
                if find:
                   out.write(str(index)+"\t"+find.group(0)+"\n")

if __name__ == '__main__':
    find()
