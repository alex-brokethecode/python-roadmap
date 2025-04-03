# Platform-Specific Output: Write a Python program that prints a different message depending on the operating system platform (e.g., Windows, Linux, macOS).

import sys

platform = sys.platform

platforms_dict = {
    'win32': 'Windows',
    'linux': 'Linux',
    'darwin': 'macOS'
}

message = platforms_dict.get(platform, 'Unknown Platform')

print(f'{platform} = {message}')
