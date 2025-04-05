# Read from input.txt, convert to uppercase, and write to output.txt

try:
    with open("input.txt", "r") as infile:
        content = infile.read()
        modified_content = content.upper()  # Modify the content (e.g., make uppercase)

    with open("output.txt", "w") as outfile:
        outfile.write(modified_content)
    print("File has been successfully modified and saved to 'output.txt'.")

except FileNotFoundError:
    print("Error: 'input.txt' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

filename = input("Enter the name of the file to read: ")

try:
    with open(filename, "r") as file:
        print("\nFile content:\n")
        print(file.read())

except FileNotFoundError:
    print(f"❌ File '{filename}' not found.")
except PermissionError:
    print(f"⚠️ You don’t have permission to read '{filename}'.")
except Exception as e:
    print(f"⚠️ An unexpected error occurred: {e}")
