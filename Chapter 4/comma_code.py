#! /usr/bin/python
#
# ATBS2E - Chapter 4 - Comma Code
#
# Say you have a list value like this:
# spam = ['apples', 'bananas', 'tofu', 'cats']
#
# Write a function that takes a list value as an argument and returns a string
# with all the items separated by a comma and a space, with 'and' inserted before
# the last item. For example, passing the previous spam list to the function
# would return 'apples, bananas, tofu, and cats'. But your function should be
# able to work with any list value passed to it. Be sure to test the case where
# an empty list [] is passed to your function.

oats = []
milk = ['apples']
hash = ['apples', 'bananas']
spam = ['apples', 'bananas', 'tofu', 'cats']
eggs = ['apples', 'bananas', 'tofu', 'cats', 'sushi', 'ommelette']

def commacode(list):
    string = ''
    if len(list) == 0:
        print('Error: List is empty')
    elif len(list) == 1:
        string += list[0]
        print('String returned:')
        print(string)
        return(string)
    elif len(list) == 2:
        string = str(list[0]) + ' and ' + str(list[1])
        print('String returned:')
        print(string)
        return(string)
    elif len(list) >= 3:
        for i in range(len(list[:-1])):
            list[i] += ', '
        list.insert(-1, 'and ')
        for i in range(len(list)):
            string += list[i]
        print('String returned:')
        print(string)
        return(string)

commacode(oats)
print()
commacode(milk)
print()
commacode(hash)
print()
commacode(eggs)
print()
commacode(spam)
