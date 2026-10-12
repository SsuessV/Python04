import sys
import typing

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <file>")
else:
    print("=== Cyber Archives Recovery ===")
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
    except OSError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
