# Input:
#   mylist = [20, 100, 20, 1, 10]
# Output:
#   smallest is 1
#   largest is 100

# Approach 1: Sort the list in ascending order and print the fist and last elements in the list
mylist = [20, 100, 20, 1, 10]
# mylist.sort()   # [1, 10, 20, 20, 100]
# print(mylist)
#
# print("The smallest element is:", mylist[0])    # 1
# print("The largest element is:", mylist[-1])    # 100

# Approach 2: min() and max() methods
print("The smallest element is:", min(mylist))
print("The largest element is:", max(mylist))

