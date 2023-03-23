# Approach 1: Loop

mylist = [1, 6, 3, 5, 3, 4]
ele = 5
# flag = 0
#
# for i in mylist:
#     if i == ele:
#         print("Element found")
#         flag = 1
#         break
#
# if flag == 0:
#     print("Element not found")

# Approach 2: in operator

if ele in mylist:
    print("Element found")
else:
    print("Element not found")