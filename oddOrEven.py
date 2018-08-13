def oddOrEven(arr):
    return 'even' if sum(arr,0) % 2 == 0 else 'odd'
print(oddOrEven([0, 1, 3]))