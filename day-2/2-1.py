safe_count = 0

def is_asc(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

def is_desc(arr):
    return all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1))

with open("input.txt", "r") as file:
    for line in file:
        report = list(map(int, line.split()))
        if is_asc(report) or is_desc(report):
          for i in range(len(report) - 1):
                difference = abs(report[i] - report[i + 1])
                if not (0 < difference < 4):
                  break
          else:
              safe_count += 1

print(safe_count)