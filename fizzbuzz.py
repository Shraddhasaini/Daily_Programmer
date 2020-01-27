for x in range(100):
    if x % 3 == 0  and x % 5 == 0 :
        print("fizzbuzz")
        continue
    elif x % 5 == 0:
        print("buzz")
        continue
    elif x % 3 == 0 :
        print("fizz")
        continue
    else: print(x)
