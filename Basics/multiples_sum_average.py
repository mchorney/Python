# Odd Numbers 1 to 1000 in a "for loop"

for x in range(1, 1000, 2):
    print x

# Multiples of five 5 to 1,000,000

for x in range(0, 1000001, 5):
    print x

# Sum of List
a = [1, 2, 5, 10, 255, 3]
sum = 0
for i in a:
    sum += i
print sum

#Average of a List of Numerical Elements

a = [1, 2, 5, 10, 255, 3]
sum = 0
length = len(a)
for i in a:
    sum += i
print "Average: ", sum / length
