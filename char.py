#Write a Python program to get a string from a given string
#where all occurrences of its first char have been changed to
#'$', except the first char itself.
given = 'thisisthegivenstring'
print(given[0] + given.replace(given[0],'$')[1:])
