# remove nth occurrence of "geeks"
mylist = ["geeks", "for", "geeks", "geeks", "geeks"]
word = "geeks"
n = 3   # nth occurrence

count = 0

for i in range(0, len(mylist)-1):
    if mylist[i] == word:
        count += 1   # 1  2
        if count == n:
            del mylist[i]
print("Updated list:", mylist)
