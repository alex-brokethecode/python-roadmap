# Implement a custom version of map(), filter(), and reduce() using loops and list comprehensions.

# [ Tip ]
# Using yield makes these functions lazy (they generate values on demand instead of creating full lists).

def custom_map(lst, function):
    # return [function(i) for i in lst] # [ My Solution ]

    # [ Improved version]
    for i in lst:
        yield function(i)


def custom_filter(lst, condition):
    # return [i for i in lst if condition(i)] # [ My Solution ]

    # [ Improved version ]
    for i in lst:
        if condition(i):
            yield i


def custom_reduce(lst, function):
    output = lst[0]
    for i in lst[1:]:
        output = function(output, i)

    return output


numbers = [i for i in range(1, 11)]

square = list(custom_map(numbers, lambda x: x ** 2))
even = list(custom_filter(numbers, lambda x: x % 2 == 0))
total = custom_reduce(numbers, lambda x, y: x + y)

print(f'{square=}')
print(f'{even=}')
print(f'{total=}')
