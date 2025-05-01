from Words import sentence_parts
from functools import reduce
print(reduce((lambda x, y : x + " " + y), sentence_parts))
