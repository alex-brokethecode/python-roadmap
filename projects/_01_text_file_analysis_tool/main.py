from pathlib import Path
from string import punctuation
from re import sub
from collections import Counter


def read_file(filename: str) -> str:
    """Reads the content of a file and returns it as a string.

    Args:
        filename: The name of the file to read.

    Returns:
        The content of the file as a string.

    Raises:
        FileNotFoundError: If the file is not found.
    """
    current_directory = Path(__file__).parent
    file_path = current_directory / filename

    try:
        with open(file_path, 'r') as file:
            lines = file.read()
    except FileNotFoundError:
        raise FileExistsError(f'"{filename}" file not found')
    else:
        return lines


def clean_text(text: str) -> str:
    """Cleans the text by lowercasing, removing punctuation, and replacing newlines with spaces.

    Args:
        text: The text to clean.

    Returns:
        The cleaned text.
    """
    # Remove leading and trailing whitespace and convert to lowercase
    text = text.strip().lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', punctuation))
    # Replace newlines and indentation with spaces
    text = sub(r'\s+', ' ', text)
    return text


def calculate_words_count(text: str) -> int:
    """Calculates the number of words in the given text.

    Args:
        text: The text to analyze.

    Returns:
        The number of words in the text.
    """
    cleaned_text = clean_text(text)

    return len(cleaned_text.split())


def calculate_lines_count(text: str) -> int:
    """Calculates the number of lines in the given text.

    Args:
        text: The text to analyze.

    Returns:
        The number of lines in the text.
    """
    return len(text.splitlines())


def calculate_characters_count(text: str) -> int:
    """Calculates the total number of characters in the given text.

    Args:
        text: The text to analyze.

    Returns:
        The total number of characters in the text.
    """
    return len(text)


def calculate_words_frequency(text: str) -> dict:
    """Calculates the frequency of each word in the given text.

    Args:
        text: The text to analyze.

    Returns:
        A dictionary where keys are words and values are their frequencies.
    """
    cleaned_text = clean_text(text)
    words = cleaned_text.split()

    return dict(Counter(words))


def main() -> None:
    try:
        original_text = read_file('sample.txt')
        cleaned_text = clean_text(original_text)

        print(f'Words count: {calculate_words_count(cleaned_text)}')
        print(f'Lines count: {calculate_lines_count(original_text)}')
        print(f'Characters count: {calculate_characters_count(original_text)}')
        print(f'Words Frequency: {calculate_words_frequency(cleaned_text)}')

    except FileNotFoundError as e:
        print(e)


if __name__ == '__main__':
    main()
