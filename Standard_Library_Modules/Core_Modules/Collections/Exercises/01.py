# Word Frequency: Write a Python program that takes a sentences as input
# and uses collections.Counter to count the frequency of each word

import collections


def count_words(sentence: str) -> dict[str, int]:
    return collections.Counter(sentence.split())


def count_words2(sentence: str) -> dict[str, int]:
    counter = {}
    for char in sentence.split():
        counter[char] = counter.get(char, 0) + 1
    return counter


if __name__ == '__main__':
    sentence = 'apple banana apple orange banana apple'
    print(count_words(sentence))
    print(count_words2(sentence))
