# File Input with Exception Handling: Write a Python program that prompts the user for a filename, attempts to open the file, reads its content, and prints it. Handle both FileNotFoundError and IOError exceptions.

try:
    with open(file=input('Filename: '), mode='r+') as file:
        content = file.read()
        print(content)
except FileNotFoundError as e:
    print(f'Error: {e}')
except IOError as e:
    print(f'Error: {e}')
except Exception as e:
    print(f'Error: {e}')

# IOError is a general exception and include exceptions like:
# - Disk Errors, Permission Errors, Network Errors, Device Errors, Invalid File Operations
