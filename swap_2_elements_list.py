# Approach 1: simple swap

mylist = [23, 65, 19, 90]  # index starts from 0
print(mylist)
pos1, pos2 = 1, 3   # 65, 90
# mylist[pos1], mylist[pos2] = mylist[pos2], mylist[pos1]     # 90, 65

# Approach 2: built-in list.pop() function

# first_ele = mylist.pop(pos1)    # 65  -> 23, 19, 90
# second_ele = mylist.pop(pos2-1)   # 90  -> 23, 19
# mylist.insert(pos1, second_ele)
# mylist.insert(pos2, first_ele)


# Approach 3: Tuple

get = (mylist[pos1], mylist[pos2])  # packing: 65, 90
mylist[pos2], mylist[pos1] = get  # unpacking: 90, 65


print(mylist)

