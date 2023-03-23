# Input: mylist = [70, 11, 20, 4, 100]
# Output : 70

# Approach 1: sort()
mylist = [10, 20, 4, 45, 99]
# mylist.sort()
# print(mylist)   # [4, 10, 20, 45, 99]
# print("Largest number is:", mylist[-1])
# print("Second largest number is:", mylist[-2])

# Approach 2: set()
new_list = set(mylist)      # {99, 4, 10, 45, 20}
new_list.remove(max(new_list))     # None, b/c 99 is removed
print(new_list)     # {4, 10, 45, 20}
print(max(new_list))    # 45
