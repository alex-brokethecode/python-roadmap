# Given a list of names, remove duplicates while keeping the original order.

countries: list[str] = ['Sweden', 'Denmark', 'Finland',
                        'Sweden', 'Norway', 'Denmark', 'Iceland']

seen: set = set()
unique_countries: list[str] = []

for country in countries:
    if country not in seen:
        unique_countries.append(country)
        seen.add(country)

print(unique_countries)
