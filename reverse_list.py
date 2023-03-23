# Input: [10, 11, 12, 13, 14, 15]
# Output: [15, 14, 13, 12, 11, 10]


# Approach 1: use reverse() method
mylist = [10, 11, 12, 13, 14, 15]
print("List before reversal:", mylist)
# mylist.reverse()
# print("List after reversal:", mylist)

# Approach 2: slicing technique
# [start_point : end_point : step_value]
# [::] no start or end points will consider all elements

mylist2 = mylist[::-1]

print("List after reversal:", mylist2)
