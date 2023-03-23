# Substring Presence in Given String
# str = "welcome to python programming"
# sub_str = "python"

# The find() me hod finds the first occurrence of the specified value.
# The find() method returns -1 if the value is not found.

my_str = "welcome to python programming"
my_substr = "python"

print(my_str.find(my_substr))   # 11 - the position where "python" is started

if my_str.find(my_substr) == -1:
    print("Not found")
else:
    print("Found")
