# Find length of a String
# Input: welcome
# Output:7


# Approach 1: for loop
my_str = "welcome"
counter = 0
# for i in my_str:
#     counter += 1


# Approach 2: while loop and slicing
# while my_str[counter:]:     # 0:6->1:6->2:6->3:6->4:6->5:6->6:6
#     counter += 1
# print(counter)      # 7

# Approach 3: len() built-in function
# print(len(my_str))      # 7

# Approach 4: join() and count()
random_str = "X"

print(random_str.join(my_str))    # wXeXlXcXoXmXe
print(random_str.join(my_str).count(random_str))    # 6
print(random_str.join(my_str).count(random_str) + 1)    # 7

my_str = "Welcome To Python"
print(random_str.join(my_str))    # WXeXlXcXoXmXeX XTXoX XPXyXtXhXoXn
print(random_str.join(my_str).count(random_str))    # 16
print(random_str.join(my_str).count(random_str) + 1)    # 17
