from Scores import scores
from functools import reduce
Scores_List = []
for i in scores:
    Scores_List += list(dict(i).values())
print(reduce(lambda x, y : x+y, Scores_List))
