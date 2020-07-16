#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b.
import re
if re.search('a.*?b$',  'a end with b'):
    print('match')
