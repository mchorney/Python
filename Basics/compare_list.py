# Write a program that compares two lists and prints a message depending on if
# the inputs are identical or not.

list_one = ['celery', 'carrots', 'bread', 'milk']
list_two = ['celery', 'carrots', 'bread', 'cream']


def compareLists(lst1, lst2):

    if sorted(list_one) == sorted(list_two):
        print "The lists are the same"

    else:
        print "The lists are not the same"


compareLists(list_one, list_two)
