# Approach 1: Temporary variable

mylist = [12, 35, 9, 56, 24]        # index starts from 0

# size = len(mylist)      # 5
# temp = mylist[0]
# mylist[0] = mylist[size-1]
# mylist[size-1] = temp


# Approach 2:

# mylist[0], mylist[-1] = mylist[-1], mylist[0]

# Approach 3: Tuple
# get = (mylist[-1], mylist[0])     # packing: 24, 12
# mylist[0], mylist[-1] = get      # unpacking


# Approach: * operand

# start, *middle, end = mylist
#
# print(start)    # 12
# print(middle)   # [35, 9, 56]
# print(end)  # 24
#
# mylist = [end, *middle, start]


# Approach 5: pop() built-in function

first = mylist.pop(0)   # 12
last = mylist.pop(-1)   # 24

mylist.insert(0, last)
mylist.append(first)


print("List after swapping:", mylist)
