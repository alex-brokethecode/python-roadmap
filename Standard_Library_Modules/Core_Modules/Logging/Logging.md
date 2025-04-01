# logging Module

## Theory

The `logging` module provides a flexible framework for emitting log messages from Python programs. It allows you to control the level of detail in your logs, format log messages, and send logs to various destinations (e.g., console, files, network).

### Log Levels

- `DEBUG`: Detailed information, typically of interest only when diagnosing problems.
- `INFO`: Confirmation that things are working as expected.
- `WARNING`: An indication that something unexpected happened, or indicative of some problem in the near future.
- `ERROR`: Due to a more serious problem, the software has not been able to perform some function.
- `CRITICAL`: A serious error, indicating that the program itself may be unable to continue running.

### Loggers

- Loggers are the primary interface for emitting log messages.
- `logging.getLogger(name)`: Creates or retrieves a logger with the specified name.

### Handlers

- Handlers determine where log messages are sent (e.g., console, files).
- `logging.StreamHandler()`: Sends log messages to the console.
- `logging.FileHandler(filename)`: Sends log messages to a file.

### Formatters

- Formatters specify the layout of log messages.
- `logging.Formatter(format)`: Creates a formatter with the specified format string.

### Basic Configuration

- `logging.basicConfig(...)`: Configures basic logging settings.

### Example

```python
import logging

# Configure basic logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Create a logger
logger = logging.getLogger(__name__)

# Log messages
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
```

## Exercises

### Easy

1. **Basic Logging:** Write a Python program that uses the logging module to log messages at different levels (DEBUG, INFO, WARNING, ERROR, CRITICAL). [Solution](./Exercises/01.py)

### Medium

2. **File Logging:** Write a Python program that logs messages to a file instead of the console. [Solution](./Exercises/02.py)

### Hard

3. **Custom Formatting:** Write a Python program that logs messages with a custom format, including the timestamp, log level, and message. [Solution](./Exercises/03.py)
