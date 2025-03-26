# Extract information from Log Files: Given a log file with entries like [INFO] 2023-10-26 10:00:00 - User logged in. Write a Regular expression to extract the log level, timestamp and message

from re import compile, search


def get_data_from_log(log: str) -> tuple[str, str, str]:
    pattern = compile(
        r'\[(\w+)\] (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - (.+)')
    match = search(pattern, log)

    if match:
        return match.group(0), match.group(1), match.group(2)
    else:
        return '', '', ''


level, timestamp, message = get_data_from_log(
    '[INFO] 2023-10-26 10:00:00 - User logged in.')
