#!/usr/bin/env python3
# Author ID: 113852222

def append_file_string(file_name, string_of_lines):
    """Appends the string_of_lines to the end of the file."""
    with open(file_name, 'a') as f:
        f.write(string_of_lines)

def write_file_list(file_name, list_of_lines):
    """Writes all items from list_of_lines to file where each item is one line."""
    with open(file_name, 'w') as f:
        for line in list_of_lines:
            f.write(line + '\n')

def copy_file_add_line_numbers(file_name_read, file_name_write):
    """Reads data from first file, writes to second file with line numbers."""
    with open(file_name_read, 'r') as f_read:
        lines = f_read.readlines()
    
    with open(file_name_write, 'w') as f_write:
        for index, line in enumerate(lines, start=1):
            f_write.write(f"{index}:{line}")

def read_file_string(file_name):
    """Reads the content of a file and returns it as a string."""
    with open(file_name, 'r') as f:
        return f.read()

def read_file_list(file_name):
    """Reads a file and returns a list of all lines without newline characters."""
    try:
        with open(file_name, 'r') as f:
            return [line.strip() for line in f.readlines()]  # Strip newline characters
    except Exception as e:
        return f'error: could not read file {file_name}, reason: {str(e)}'

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    
    append_file_string(file1, string1)
    print(read_file_string(file1))
    
    write_file_list(file2, list1)
    print(read_file_string(file2))
    
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))
