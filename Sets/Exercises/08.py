# Count how many times each word appears in "apple banana apple orange banana apple" and store the result in a set.

sentence = "apple banana apple orange banana apple"

# [ My Solution ]

words = sentence.split(' ')
counter = {}

for word in words:
    counter[word] = counter.get(word, 0) + 1

values = set(counter.values())
print(values)
