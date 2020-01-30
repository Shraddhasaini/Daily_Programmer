a = [int(x) for x in input("Enter score: ").split()]
print(sorted(list(set(a)))[-2])
