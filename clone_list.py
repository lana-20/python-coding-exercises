# Clone / Copy a List
# Input: mylist = [4, 8, 2, 10, 15, 18]
# Output: mylist_copy = [4, 8, 2, 10, 15, 18]


# Approach 1: slicing technique

mylist = [4, 8, 2, 10, 15, 18]
# mylist_copy = mylist[:]  # without Start & end index it reads from beginning to end


# Approach 2: extend() method

# mylist_copy = []
# mylist_copy.extend(mylist)


# Approach 3: list() method

# mylist_copy = list(mylist)


# Approach 4: copy() method

# mylist_copy = mylist.copy()


# Approach 5: list comprehension

mylist_copy = [i for i in mylist]


print(mylist_copy)
