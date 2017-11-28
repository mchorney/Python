# Odd and Even Numbers between 1 and (function range variable)


def oddeven(number):

    for x in range(1, (number)):

        if x % 2 == 0:
            print "Number is ", x, "This is an even number."
        else:
            print "Number is ", x, "This is an odd number."


#
oddeven(1001)  # Line to execute function


#Mulitply: list iteration finding mulitples of the number 5

a = [2, 4, 10, 16]
new = list()


def multiply(x, y):
    for z in x:
        z *= y
        new.append(z)


multiply(a, 5)  # Calls Function

print new  # Prints new Array
