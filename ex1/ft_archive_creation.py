import sys
import typing

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <file>")
else:
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{sys.argv[1]}'")
    try:
        file: typing.IO = open(sys.argv[1], "r")
        print("---")
        print()
        content = file.read()
        print(content)
        print()
        print("---")
        file.close()
        print(f"File '{sys.argv[1]}' closed.")
        print()
        print("Transform data:")
        print("---")
        print()
        lines = [line + "#" for line in content.splitlines()]
        transformed = "\n".join(lines)
        print(transformed)
        print()
        print("---")
        new_file_name = input("Enter new file name (or empty): ")
        if new_file_name:
            try:
                print(f"Saving data to '{new_file_name}'")
                new_file: typing.IO = open(new_file_name, "w")
                new_file.write(transformed + "\n")
                new_file.close()
                print(f"Data saved in file '{new_file_name}'.")
            except OSError as e:
                print(f"Error writing to file '{new_file_name}': {e}")
        else:
            print("Not saving data.")
    except OSError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
