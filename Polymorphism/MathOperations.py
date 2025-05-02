class MathOperations():
    def calculate(self, *args):
        if len(args) == 2:
            return args[0] + args[1]
        elif len(args) == 3:
            return args[0] * args[1] + args[2]
        else:
            return "Invalid Length of Arguments!"
