def longest_consec(strarr, k):
    if len(strarr) == 0 or k > len(strarr) or k <= 0:
        return '' 
    r = sorted(strarr, key = len ,reverse = True)
    index = strarr.index(r[0])
    print(index)
    if (index + k) > len(strarr)-1:
        for i in range(k):
            print("i = ",i)
            result = strarr[index - i] + r[0]
    else:
        for j in range(k):
            result = r[0] + strarr[index + j]
    return result
print(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1))
