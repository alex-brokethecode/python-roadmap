# Group by First Letter: Write a Python program that takes a list of words as input
# and uses collections.defaultdict to group the words by their first letter

import collections


def group_by_first_letter(words: list[str]) -> dict[str, list[str]]:
    """Using collections.defaultdict to group the words by their first letter."""
    output = collections.defaultdict(list)  # list = default factory

    for word in words:
        output[word[0]].append(word)  # Get value from dict and append word

    return output


def group_by_first_letter2(words: list[str]) -> dict[str, list[str]]:
    """"Using dict to group the words by their first letter. Explicit declaration (do the same as defaultdict."""
    output = {}
    for word in words:
        first_letter = word[0]
        if first_letter not in output:
            output[first_letter] = []
        output[first_letter].append(word)

    return output


if __name__ == '__main__':
    words: list[str] = ['apple', 'banana', 'cherry', 'baby', 'cat', 'bubble']
    print(group_by_first_letter(words))
