def fake_bin(x):
    def replaceNum(num):
        if int(num) >= 0 and int(num) < 5:
            return '0'
        else:
            return '1'
    r = ''.join(list(map(replaceNum, x)))
    return r
print(fake_bin('45385593107843568'))

##############大佬的最佳实践
def fake_bin(x):
    return ''.join('0' if c < '5' else '1' for c in x)
