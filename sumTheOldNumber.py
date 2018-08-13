def row_sum_odd_numbers(n):
    count = 0
    first = 1
    for i in range(n):
        count = 2 * i
        first += count
        sum = 0
        for j in range(0, i + 1):
            sum += first + 2 * j
    return sum
print(row_sum_odd_numbers(13))

#大佬的最佳实践
def row_sum_odd_numbers(n):
    #your code here
    return n ** 3
        