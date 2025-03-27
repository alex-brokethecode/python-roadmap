# Regular Expressions

## Theory

Regular expressions use a special syntax to define search patterns. Here are some fundamental concepts and common patterns:

- Metacharacters: Special characters that have a specific meaning in regex.
  - `.`: Matches any single character (except newline by default).
  - `^`: Matches the beginning of a string.
  - `$`: Matches the end of a string.
  - `*`: Matches zero or more occurrences of the preceding character or group.
  - `+`: Matches one or more occurrences of the preceding character or group.
  - `?`: Matches zero or one occurrence of the preceding character or group.
  - `[]`: Matches any single character within the brackets.
  - `[^...]`: Matches any single character not within the brackets.
  - `()`: Groups parts of the regex.
  - `|`: Acts as an "OR" operator.
  - `\\`: Escapes special characters (e.g., `\.` matches a literal dot).
- Quantifiers: Specify how many times a character or group should be matched. (`*`, `+`, `?`, `{n}`, `{n,}`, `{n,m}`)
- Character Classes: Predefined sets of characters.
  - `\d`: Matches any digit (0-9).
  - `\w`: Matches any word character (alphanumeric and underscore).
  - `\s`: Matches any whitespace character (space, tab, newline, etc.).
  - `\D`: Matches any non-digit character.
  - `\W`: Matches any non-word character.
  - `\S`: Matches any non-whitespace character.
- `re` Module in Python: The built-in `re` module provides functions for working with regular expressions.
  - `re.search(pattern, string)`: Searches for the pattern anywhere in the string. Returns a match object if found, otherwise `None`.
  - `re.match(pattern, string)`: Matches the pattern at the beginning of the string. Returns a match object if found, otherwise `None`.
  - `re.findall(pattern, string)`: Finds all occurrences of the pattern in the string and returns them as a list of strings.
  - `re.finditer(pattern, string)`: Returns an iterator that yields match objects for all occurrences of the pattern.
  - `re.sub(pattern, replacement, string)`: Replaces all occurrences of the pattern with the replacement string.

**Example:**

```python
import re

text = "The quick brown fox jumps over the lazy dog."

# Search for "fox"
match = re.search(r"fox", text)
if match:
    print(f"Found: {match.group(0)}")

# Find all words
words = re.findall(r"\b\w+\b", text)
print(f"Words: {words}")

# Replace "dog" with "cat"
new_text = re.sub(r"dog", "cat", text)
print(f"New text: {new_text}")
```

## Exercises

### Easy

1. **Find Email Addresses:** Write a regular expression to find all email addresses in a given text. [Solution](./Exercises/01.py)

### Medium

2. **Validate Phone Numbers:** Write a regular expression to validate phone numbers in a specific format (e.g., xxx-xxx-xxxx). [Solution](./Exercises/02.py)

### Hard

3. Extract Information from Log Files: Given a log file with entries like `[INFO] 2023-10-26 10:00:00 - User logged in`, write a regular expression to extract the log level, timestamp, and message. [Solution](./Exercises/03.py)
