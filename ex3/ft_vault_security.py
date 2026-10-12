def secure_archive(filename, action="read", content="") -> tuple[bool, str]:
    try:
        if action == "read":
            with open(filename, "r") as file:
                content = file.read()
                return (True, content)
        elif action == "write":
            with open(filename, "w") as file:
                file.write(content)
                return (True, "Content successfully written to file")
        return (False, "Invalid action")
    except FileNotFoundError as e:
        return (False, str(e))
    except PermissionError as e:
        return (False, str(e))
    except Exception as e:
        return (False, str(e))


print("=== Cyber Archives Security ===")
print()
result = secure_archive("/not/existing/file")
print(f"Using 'secure_archive' to read from a nonexistent file:\n{result}")
print()
result = secure_archive("/etc/master.passwd")
print(f"Using 'secure_archive' to read from an inaccessible file:\n{result}")
print()
result = secure_archive("archive.txt")
print(f"Using 'secure_archive' to read from a regular file:\n{result}")
if result[0]:
    prev_content = result[1]
    write_result = secure_archive(
        "new_archive.txt", "write", prev_content)
    print(f"Using 'secure_archive' to write"
          f"previous content to a new file:\n{write_result}")
