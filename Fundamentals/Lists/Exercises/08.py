# Implement a function that removes duplicates without using set() and maintains the original order.

# [ My Solution ]
def remove_duplicates(a_list: list[str]) -> list[str]:
    unique_items: list[str] = []

    for item in a_list:
        if item not in unique_items:
            unique_items.append(item)

    return unique_items

# [ Improved Solution ]


def remove_duplicates_2(a_list: list[str]) -> list[str]:
    # dict.fromkeys(a_list, None) => {'Sweden': None, 'Denmark': None, 'Finland': None, 'Norway': None, 'Iceland': None}
    # list(dict.fromkeys(a_list, None)) => ['Sweden', 'Denmark', 'Finland', 'Norway', 'Iceland']
    return list(dict.fromkeys(a_list, None))


# [ Execution ]
countries: list[str] = ['Sweden', 'Denmark', 'Finland',
                        'Sweden', 'Norway', 'Denmark', 'Iceland']

print(remove_duplicates(countries))
print(remove_duplicates_2(countries))
