# Ordered Word Counter: Write a Python program that takes a sentence as input and uses collections.OrderedDict
# to count the frequency of each word, maintaining the order in which the words first appear in the sentence.

from collections import OrderedDict


def count_frequency(sentence: str) -> OrderedDict:
    words = sentence.split()

    ordered = OrderedDict()

    for word in words:
        ordered[word] = 1 + ordered.get(word, 0)

    return ordered


sentence = 'banana apple orange banana apple'
print(count_frequency(sentence))
