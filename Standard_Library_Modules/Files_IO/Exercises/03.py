# File Reader with Errors Handling: Write a Python program that attempts to read a file specified by the user. Implement error handling to catch `FileNotFoundError` if the file does not exist and print and informative message

def read_file(filename: str) -> None:
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f'"{filename}" content: ')
            print(content)
    except FileNotFoundError:
        print(f'File "{filename}" not found.')


read_file('output.txt')
