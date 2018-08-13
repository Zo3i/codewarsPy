def sort_array(source_array):
    odd = sorted(list(filter(lambda x: x % 2 ==1, source_array)))
    j = 0
    strs = ''.join(str(e) for e in source_array)
    for i in source_array:
        if i % 2 == 1:
            print('i=',i)
            print(odd[j])
            strs = strs.replace(str(i), str(odd[j]))
            j += 1
        
    print(odd)
    print(strs)

print(sort_array([5, 3, 2, 8, 1, 4]))