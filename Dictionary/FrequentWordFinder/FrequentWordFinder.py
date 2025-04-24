import Passage
words = Passage.passage.split().copy()
count = dict({})
for i in words:
    if i not in count.keys():
        count[i] = words.count(i)
numbers = list(count.values())
max = numbers[0]
for i in range(len(numbers)-1):
    if max < numbers[i]:
        max = numbers[i]
word = ""
for key, value in count.items():
    if value == max:
        word = key
print(f"{word} is the most repeated word in the passage which is repeated {max} times.")
