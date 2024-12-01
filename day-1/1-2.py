row_1 = []
row_2 = []

with open("input.txt", "r") as file:
    for line in file:
        num1, num2 = map(int, line.split())
        row_1.append(num1)
        row_2.append(num2)

sim_score = 0
for num in row_1:
    sim_score += num * row_2.count(num)

print(sim_score)