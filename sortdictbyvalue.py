#Write a Python script to sort (ascending and descending) a dictionary by value.
mydict = {
            'key1111111' : 1,
            'key111111' : 11,
            'key11111' : 111,
            'key1111' : 1111,
            'key111' : 11111,
            'key11' : 111111,
            'key1' : 1111111,
}

print('ascending: ' + str(sorted(mydict.values())) +'\n' + 'descending: ' + str(sorted(mydict.values(), reverse = True)))
