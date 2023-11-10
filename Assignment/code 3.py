def read_and_write_file(filename):
    try:
        # Read the content from the original file
        with open(filename, 'r') as file:
            content = file.read()

        # Write the uppercase content to a temporary file
        temp_filename = filename + ".tmp"
        with open(temp_filename, 'w') as temp_file:
            temp_file.write(content.upper())

        # Replace the original file with the temporary file
        import os
        os.replace(temp_filename, filename)

        print(f"File '{filename}' processed successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    filename = "Sample.txt"
    read_and_write_file(filename)

if __name__ == "__main__":
    main()
