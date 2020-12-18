#%% if/elif/else statements - do code under certain conditions
if 1 == 2:
    print("statement is true")
    x = 3
    print(x)
print("back to normal")

#%%
n = 0
if n > 8:  # start with this
    print("n is greater than 8")
elif 3 <= n <= 8:  # as many elif's as you like
    print("n is between 3 and 8")
elif 1 < n < 3:
    print("n is between 1 and 3")
else:  # optional
    print("n is smaller then 1")
    
#%% for loops
names = ["Matthew", "Carolina", "Szabina", "Milou", "Swan"]
depts = ["OCS", "EDS", "OCS", "MMB", "MMB"]
numbers = [5, 1, 78, 3, 11, 5, 2]

for n in range(len(names)):
    print(names[n])
    
# # shorthand for:    
# print(name[0])
# print(name[1])
# # etc.

for name in names:
    print(name)

#%% Loop through multiple things
for i, name in enumerate(names):
    print(i, name, depts[i])
    
#%% Another way to go through multiple things
for name, dept, number in zip(names, depts, numbers):
    print(name, dept, number)
    
#%% More powerful iterators
# https://docs.python.org/3/library/itertools.html
from itertools import product
for name, dept in product(names, depts):
    print(name, dept)

#%% Strings are iterables too
for letter in names[1]:
    print(letter)

#%% Iteration through dicts
names = ["Matthew", "Carolina", "Szabina", "Milou", "Swan"]
depts = ["OCS", "EDS", "OCS", "MMB", "MMB"]
info = {name: dept for name, dept in zip(names, depts)}

# Iterating through the dict just gets the keys
for key in info:
    print(key)
for key in info.keys():  # more long winded of above
    print(key)

for value in info.values():  # get the values
    print(value)

for k, v in info.items():  # get keys and values
    print(k, v)

# There are pandas tools too - iterrows() and iteritems()

#%% Final for loops stuff
for x in reversed(names):
    print(x)
    if x == "Szabina":
        break
    
#%% While loop
while 1 == 2:  # infinite loop if 1 == 1
    print("AAAAaAAAaaaaAAAAaAAAaaaaAAAAaAAAaaaaAAAAaAAAaaaa")


for x in range(5):
    print(x)

x = 0
while x <= 4:
    print(x)
    x += 1

names = ["Matthew", "Carolina", "Szabina", "Milou", "Swan"]
i = 0
name = names[i]
while name != "Szabina":
    print(name)
    i += 1
    name = names[i]
