def get_filename_and_read():
    filename = input("Please enter the filename you want to read: ")
    
    try:
        # Step 1: Try opening the file and reading it
        with open(filename, 'r') as file:
            content = file.read()
        print("File content successfully read!")
        print("\nContent of the file:")
        print(content)
    
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
    except IOError:
        print(f"Error: There was an issue reading the file {filename}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
get_filename_and_read()
