list1, list2 = [], []

with open('data/01', 'r') as f:
    while line := f.readline():
        num1, num2 = line.split()
        list1.append(int(num1))
        list2.append(int(num2))

list1.sort(), list2.sort()
difference, similarity = 0, 0

for i in range(len(list1)):
    difference += abs(list1[i] - list2[i])
    similarity += list1[i] * list2.count(list1[i])

print(f"Difference score: {difference}")
print(f"Similarity score: {similarity}")
