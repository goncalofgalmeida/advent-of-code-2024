import numpy as np

row_1 = []
row_2 = []

with open("input.txt", "r") as file:
    for line in file:
        num1, num2 = map(int, line.split())
        row_1.append(num1)
        row_2.append(num2)

row_1 = np.array(row_1)
row_2 = np.array(row_2)

row_1.sort()
row_2.sort()

diff_output = np.abs(row_2 - row_1)
result = np.sum(diff_output)

print(result)