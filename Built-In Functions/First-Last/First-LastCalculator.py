from list import numbers
from functools import reduce
print(reduce(lambda x, y : x-y, [numbers[0], numbers[-1]]))
