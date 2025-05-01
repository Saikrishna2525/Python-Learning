from NumbersList import numbers
from functools import reduce
print(reduce((lambda num1, num2 : num1*num2), numbers))
