def typelist(x):

    sum = 0
    string = ''

    if (isinstance(i, int) or isinstance(i, float) for i in x):
        print "The list you entered is of integer type."

    elif (isinstance(i, str) for i in x):
        print "The list you entered is of string type."

    for i in x:

        if type(i) is int:
            sum += i
            print 'Sum:' + str(sum)

        if type(i) is str:
            string += ',' + i
            print string


typelist(['magical unicorns', 19, 21, 'hello', 98.98, 'world'])
