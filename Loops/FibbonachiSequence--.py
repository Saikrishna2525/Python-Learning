number = int(input("How many numbers do you want to show in fibbonachi series: "))
number_sequence = 1
sequence = []
sequence.append(1)
for i in range(1, number):
    number_sequence = sequence[len(sequence)-2:len(sequence)-1]
    sequence.append(number_sequence)
print(sequence)
