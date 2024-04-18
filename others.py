# DateTime

import datetime
import re

a = datetime.datetime.now()
print(a.strftime("%A"))

# Math

a = min(10, 20, 30, 40, 50, 100)
b = max(50, 10, 60, 100, 70, 80)
print(a)
print(b)
print(abs(-100))
print(pow(5, 2))

# Python RegEx

text = "My name is ashik,Ashik is the best,no 1"
a = re.findall("[A-Z]", text)
print(a)
b = re.findall("^1", text)
if b:
    print("Yes")
else:
    print("Not in start")

# File create,read file,write file
# Module
