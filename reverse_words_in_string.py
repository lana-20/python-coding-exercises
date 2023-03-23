# Input:
# str="welcome to python programming"
# Output:
# programming python to welcome

my_str = "welcome to python programming"
words = my_str.split(" ")
print(words)    # ['welcome', 'to', 'python', 'programming']

words = words[-1::-1]
# the 1st -1 represents reversing the str
# the 2nd -1 represents going back from to the first position

print(words)    # ['programming', 'python', 'to', 'welcome']

output_str = " ".join(words)

print(output_str)   # programming python to welcome
