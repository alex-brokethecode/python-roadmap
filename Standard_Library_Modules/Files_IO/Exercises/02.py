# Write to a File: Write a Python program that takes a string as input and write it to a new file named "output.txt"

def write_to_file(filename: str, string: str) -> None:
    with open(filename, 'w') as file:
        file.write(string)


def read_file(filename: str) -> None:
    with open(filename, 'r') as file:
        content = file.read()
        print(content)


try:
    write_to_file('output.txt', 'Python is fun')
    read_file('output.txt')
except Exception as e:
    print(e)
