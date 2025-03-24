# Write a lambda function that takes a number and returns its cube.

# [ My Solution ]

# fmt: off
cube = lambda x: x ** 3  # autopep8 will ignore this line

# fmt: on
print(cube(3))

# [ Tip ]
print((lambda x: x ** 3)(3))
