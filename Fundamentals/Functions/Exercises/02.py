# Use map() to convert a list of temperatures in Celsius to Fahrenheit.

def celsius_to_fahrenheit(celsius: float) -> float:
    return celsius * 9/5 + 32


celsius: list[float] = [-10, 0, 10, 20, 37]

# fahrenheit: list[float] = list(map(lambda x: celsius_to_fahrenheit(x), celsius))
fahrenheit: list[float] = list(map(celsius_to_fahrenheit, celsius))
print(f'{fahrenheit=}')
