def read_and_modify_file():
    # Prompt the user for the input filename
    input_filename = input("Enter the name of the file to read: ")

    try:
        # Attempt to open and read the file
        with open(input_filename, 'r') as infile:
            content = infile.read()

        # Modify the content (for example, converting it to uppercase)
        modified_content = content.upper()

        # Create a new output file to write the modified content
        output_filename = "modified_" + input_filename
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Modified content written to '{output_filename}' successfully.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except IOError:
        print(f"Error: The file '{input_filename}' could not be read or written.")

# Run the function
read_and_modify_file()
