def count_positives_sum_negatives(arr):
    list1 = len(list(filter(lambda x: x > 0,arr)))
    list2 = sum(list(filter(lambda x: x <= 0,arr)))
    return [] if len(arr) == 0 else [list1, list2]
print(count_positives_sum_negatives([0, 0]))