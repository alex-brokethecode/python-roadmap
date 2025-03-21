# Count the frequency of words in a sentence and store the result in a dictionary.

sentence: str = "apple banana apple orange banana apple"

# [ My Solution ]
output: dict[str, int] = {}

for word in set(sentence.split(' ')):
    output[word] = sentence.count(word)

print(output)

# [ Improved Version ]

output = {}
words = sentence.split(' ')

for word in words:
    output[word] = output.get(word, 0) + 1
    # Value stores 0 + 1 the first time, and then add 1 to the previous value

print(output)
