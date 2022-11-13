numbers = []

for i in range (1, 1000000003):
    if i % 3 == 0:
        if (str(i)[-1] != '4') or (str(i)[-1] != 7):
            numbers.append(i)
print(sum(numbers))
