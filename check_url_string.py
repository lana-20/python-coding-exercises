# Check for URL in a String
# str = "I'm a blogger at http://www.lanabegunova.com/"
# str = "My profile: https://daisyladybug.com/about.html"
# str = "My Profile: https://daisyladybug.com/about.html and My blog: http://www.lanabegunova.com/"

import re

my_str1 = "I'm a blogger at http://www.lanabegunova.com/"
my_str2 = "My profile: https://daisyladybug.com/about.html"
my_str3 = "My Profile: https://daisyladybug.com/about.html and My blog: http://www.lanabegunova.com/"

# https://urlregex.com/
# http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+

url1 = re.findall("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", my_str1)
print(url1)      # ['http://www.lanabegunova.com/']

url2 = re.findall("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", my_str2)
print(*url2)      # https://daisyladybug.com/about.html

url3 = re.findall("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", my_str3)
print(*url3, sep=", \n")      # https://daisyladybug.com/about.html, 	http://www.lanabegunova.com/

