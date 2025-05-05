class MathOperations():
    def calculate(self, *args):
        if len(args) == 2:
            return args[0] + args[1]
        elif len(args) == 3:
            return args[0] + args[1] + args[2]
        else:
            return "Invalid Length of Arguments!"
Calculation = MathOperations()
print(Calculation.calculate(7, 8, 9))
