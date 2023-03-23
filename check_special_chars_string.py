# Check if a string contains any special character
# Input: "welcome@@2To%%Python**Programming@!!^%%@$"
# Output: String contains Special Chars
# Input: "welcome To Python Programming"
# Output: String contains no Special Chars

import re

my_str1 = "welcome@@2To%%Python**Programming@!!^%%@$"
my_str2 = "welcome To Python Programming"
regex = re.compile("[@_!#$%^&*()<>?/\|{}~:]")

if regex.search(my_str1) == None:
    print("String 1 contains no Special Chars")
else:
    print("String 1 contains Special Chars")

if regex.search(my_str2) == None:
    print("String 2 contains no Special Chars")
else:
    print("String 2 contains Special Chars")

