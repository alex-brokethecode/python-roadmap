# Reverse a list without using the `.reverse()` method.

countries: list[str] = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']

# countries = list(reversed(countries))
countries = countries[::-1]

print(countries)
