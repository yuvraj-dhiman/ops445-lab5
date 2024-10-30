#!/usr/bin/env python3
# Author ID: 113852222

def add(number1, number2):
    try:
        # Convert inputs to float and add them
        return float(number1) + float(number2)
    except ValueError:
        return 'error: could not add numbers'

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            # Return a list of all lines in the file
            return file.readlines()
    except Exception:
        return 'error: could not read file'

if __name__ == '__main__':
    print(add(10, 5))                        # works
    print(add('10', 5))                      # works
    print(add('abc', 5))                     # exception
    print(read_file('seneca2.txt'))         # works (ensure this file exists)
    print(read_file('file10000.txt'))       # exception (ensure this file does not exist)
