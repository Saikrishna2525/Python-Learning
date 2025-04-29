results = [{'name': 'Alice', 'marks': 45}, {'name': 'Bob', 'marks': 65}]
print(list(filter(lambda x:x["marks"]>=50, results)))
