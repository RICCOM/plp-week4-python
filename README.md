## File Read & Write Challenge and Error Handling Lab 🖋️🧪
# Overview
This project includes two Python programs:

# File Read & Write Challenge: Reads the content from a file, modifies the content, and writes it to a new file.

# Error Handling Lab: Prompts the user for a filename, reads the file's content, and gracefully handles errors if the file doesn't exist or cannot be read.

# Requirements
  Python 3.x

# Files Included
read_and_write.py: Contains the program for reading from a file, modifying its content, and writing it to a new file.

# error_handling.py: Contains the program that asks the user for a filename, reads its content, and handles errors appropriately.

# How to Use
 # 1. File Read & Write Challenge:
  Place a file named input.txt (or any other file) in the same directory as the script.

  The program will read the content of the file, convert the text to uppercase, and write the result to output.txt.

  Example usage:

  python
  Copy
  Edit
  input_filename = "input.txt"
  output_filename = "output.txt"
  read_and_write_file(input_filename, output_filename)
# 2. Error Handling Lab:
   The program will ask you to enter the filename you wish to read.

   If the file is found, it will display its content. If there are errors (file not found or permission issues), it will handle them gracefully.

   Example usage:

   python
   Copy
   Edit
   get_filename_and_read()
   Error Handling
   The programs handle common file-related errors:

    FileNotFoundError: Handles the case when the specified file doesn't exist.

    IOError: Catches issues like permission errors or file reading problems.

    Exception: Catches any unexpected errors during execution.

# Example Output:
  For the File Read & Write Challenge:

  bash
  Copy
  Edit
  Content has been successfully written to output.txt!
  For the Error Handling Lab (with file not found):

  bash
  Copy
  Edit
  Error: The file example.txt does not exist.
  Conclusion
  This project demonstrates basic file handling in Python with added error handling to ensure a smooth user experience. The programs are designed to handle 
  file reading and writing tasks, while also gracefully managing potential errors such as missing files or permissions issues.
