# Replace "day" with "month" in string

words = "It's thanksgiving day. It's my birthday,too!"
words = words.replace("day", "month")
print words

# Min and Max from List

x = [2, 54, -2, 7, 12, 98]

min = min(x)
max = max(x)

print "Min: ", min
print "Max: ", max

# First and Last

x = [19, 2, 54, -2, 7, 12, 98, 32, 10, -3, 6]

first = x[0]
last = x[-1]

print "First: ", first
print "Last: ", last

# New List

x = [19, 2, 54, -2, 7, 12, 98, 32, 10, -3, 6]
x.sort()
new = len(x) / 2
new = x[0:new]
del x[0:len(x) / 2]
x.insert(0, new)
print x
