# Count Occurrences of an element in a list
# Input:
#   mylist = [15, 6, 7, 10, 12, 20, 10, 28, 10]
#   x = 10
# Output:
#   3
#   10 appears 3 times in a given list.


# Approach 1: Loop
mylist = [15, 6, 7, 10, 12, 20, 10, 28, 10]
x = 10
# count = 0
#
# for ele in mylist:
#     if ele == x:
#         count += 1


# Approach 2: count() method
# count = mylist.count(x)

# Approach 3: Counter() method
from collections import Counter

mydict = Counter(mylist)  # {5:1, 6:1, 7:1, 10:3, key:value, key:value, ...}
count = mydict[x]

print("{} has occurred {} times".format(x, count))
