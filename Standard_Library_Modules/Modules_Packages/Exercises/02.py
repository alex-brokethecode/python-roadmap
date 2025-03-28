# Create a Package: Create a package named my_math with two modules: addition.py and subtraction.py.
# Each module should contain a function that performs the corresponding operation.
# Then, create a script that imports and uses these modules

from my_math.addition import addition
from my_math.subtraction import subtraction


print(addition(28, 7))
print(subtraction(28, 7))
