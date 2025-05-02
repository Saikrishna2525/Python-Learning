from functools import reduce
def multiplication(*args):
    return reduce(lambda x, y: x*y, args)
