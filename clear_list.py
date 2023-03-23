# Approach 1: clear()

mylist = [6, 0, 4, 1]
print("My list before clearing:", mylist)
# mylist.clear()      # []


# Approach 2: re-initialize the list with no value
# mylist = []


# Approach 3: '*= 0' removes all elements of the list and makes it empty

# mylist *= 0


# Approach 4: del

del mylist[:]


print("My list after clearing:", mylist)