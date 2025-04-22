number = int(input("How many numbers do you want to show in fibbonachi series: "))
# number_sequence = 1
# sequence = []
# sequence.append(1)
# for i in range(1, number):
    # number_sequence = sequence[-2:-1]
    # sequence.append(number_sequence)
# print(sequence)


n1,n2=0,1
count=0

if number<=0:
   print("Please enter a positive number ")
elif number==1:
    print(n1)

else:
    while count<number:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        # count=count+1
        count+=1