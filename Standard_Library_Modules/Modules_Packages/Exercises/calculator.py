def addition(a, b): return a + b
def subtraction(a, b): return a - b
def multiplication(a, b): return a * b
def division(a, b): return a / b


print(__name__)

if __name__ == '__main__':
    a, s = 28, 7
    print(addition(a, s))
    print(subtraction(a, s))
    print(multiplication(a, s))
    print(division(a, s))
else:
    print('If you imported this module, cannot execute __name__ == "__main__"')
