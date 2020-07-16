#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b.
import re
str0 = 'a end with b'
str1 = 'not satisfying string'

if re.search('a.*?b$',  str0):
    print(match)
