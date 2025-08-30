# file_handling.py

def read_and_write_file():
    try:
        # Ask user for the file to read
        input_file = input("Enter the filename to read: ")
        
        # Open and read file
        with open(input_file, "r") as f:
            lines = f.readlines()
        
        # Modify content: add line numbers and uppercase
        modified_lines = [f"{i+1}: {line.upper()}" for i, line in enumerate(lines)]
        
        # Write to a new file
        output_file = "modified_" + input_file
        with open(output_file, "w") as f:
            f.writelines(modified_lines)
        
        print(f"✅ File successfully written to {output_file}")
    
    except FileNotFoundError:
        print("❌ Error: File not found. Please check the filename and try again.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


if __name__ == "__main__":
    read_and_write_file()

