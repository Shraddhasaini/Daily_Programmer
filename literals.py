#Write a Python program to search some literals strings in a string.
literals = ['literals','strings','integer']
str = 'This sentence contains literals strings'
for i in literals:
    if i in str: print(i + ': True')
    else: print(i + ': False')
