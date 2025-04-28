def read_and_write_file(input_filename, output_filename):
    try:
        # Step 1: Open the input file and read its content
        with open(input_filename, 'r') as file:
            content = file.read()
        
        # Step 2: Modify the content (example: convert to uppercase)
        modified_content = content.upper()
        
        # Step 3: Write the modified content to a new output file
        with open(output_filename, 'w') as file:
            file.write(modified_content)
        
        print(f"Content has been successfully written to {output_filename}!")
    
    except FileNotFoundError:
        print(f"Error: The file {input_filename} does not exist.")
    except IOError:
        print(f"Error: There was an issue reading or writing the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
input_filename = "input.txt"
output_filename = "output.txt"
read_and_write_file(input_filename, output_filename)
