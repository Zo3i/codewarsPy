def Descending_Order(num):
    print(num)
    return int(''.join(sorted(list(str(num)),reverse = True)))

print(Descending_Order(1021))