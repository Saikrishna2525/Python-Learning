from Values import numbers
from functools import reduce
print(reduce(lambda x, y : x if x > y else y, numbers))
