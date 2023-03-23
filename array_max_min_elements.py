# Input: arr[] = {10, 20, 4}
# Output: 20
# Output: 4

# find max ele
arr = [135, 23, 15, 60, 2]
max = arr[0]
n = len(arr)

for i in range(1, n):
    if arr[i] > max:
        max = arr[i]
print(max)

# find min ele
min = arr[0]

for i in range(1, n):
    if arr[i] < min:
        min = arr[i]
print(min)


