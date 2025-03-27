# Read a file: write a Python program that read the content of a file named "sample.txt" (you'll need to create this file with some text) and its content to the console.

try:
    # 'r+' throws and exception if the file doesn't exist
    with open('sample.txt', 'w+') as file:
        file.writelines(['Hello\n', 'I am learning Python\n',
                        'Gemini AI is helping me\n', 'Thank you\n'])
        file.seek(0)  # Move file pointer to the start
        file_lines = file.readlines()
        for line in file_lines:
            print(line, end='')
except Exception as e:
    print(e)
