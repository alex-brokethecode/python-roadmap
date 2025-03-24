# Find the key with the maximum value in a dictionary.

scores: dict[str, int] = {"Alice": 85, "Bob": 92, "Charlie": 78}

# [ My Solution ]

# max(scores.items(), key=lambda x: x[1]) => ('Bob', 92)
winner = max(scores.items(), key=lambda x: x[1])[0]
print(winner)
