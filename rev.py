from operator import add
a = [int(x) for x in input("Enter the number of list: ").split()]
print("INPUT IS: " + str(a))
c = list(map(add, a, reversed(a)))
print("OUTPUT IS: "+ str(c))
