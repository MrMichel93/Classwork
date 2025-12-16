"""
Mini-Program 2: File Reading
Topic: Exceptions & Files

Learning Objectives:
- Open and read files in Python
- Use different file reading methods
- Work with file contexts (with statement)
- Handle file-related exceptions

Instructions:
Complete this program to practice reading files safely.
Note: Some TODOs require you to create sample files first.
"""

# TODO 1: Create a simple text file called 'sample.txt' with a few lines
# You can do this manually or use code (shown below)
# Uncomment and run the following to create the file:
# with open("sample.txt", "w") as f:
#     f.write("Line 1: Hello World\n")
#     f.write("Line 2: Python is fun\n")
#     f.write("Line 3: File handling is easy\n")
# Write your code here:


# TODO 2: Open and read the entire content of 'sample.txt'
# Use the with statement to ensure the file is properly closed
# Hint: with open("sample.txt", "r") as file:
# Print the content
# Write your code here:


# TODO 3: Open 'sample.txt' and read it line by line
# Use a for loop to iterate through the lines
# Print each line (strip the newline character)
# Hint: for line in file:
# Write your code here:


# TODO 4: Open 'sample.txt' and use .readline() to read just the first line
# Print the first line
# Write your code here:


# TODO 5: Open 'sample.txt' and use .readlines() to get a list of all lines
# Store in a variable called 'lines' and print the list
# Write your code here:


# TODO 6: Write a try-except block to handle FileNotFoundError
# Try to open a file called 'nonexistent.txt'
# Catch the FileNotFoundError and print "File not found!"
# Write your code here:


# TODO 7: Create a function called 'safe_read_file' that:
# - Takes a filename as parameter
# - Tries to read and return the file contents
# - Returns None if the file doesn't exist
# - Uses try-except to handle the exception
# Write your code here:


# TODO 8: Test your safe_read_file function with:
# - A file that exists ('sample.txt')
# - A file that doesn't exist ('missing.txt')
# Print the results
# Write your code here:


# TODO 9: Open 'sample.txt' and read only the first 10 characters
# Hint: Use file.read(10)
# Write your code here:


# TODO 10: Create a file 'numbers.txt' with numbers (one per line)
# Then read the file and calculate the sum of the numbers
# Hint: Convert each line to an integer
# Write your code here:


# BONUS TODO: Write a function that counts the number of words
# in a text file. Test it with 'sample.txt'
# Hint: Split each line by spaces and count
# Write your code here:

