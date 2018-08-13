def xo(s):
    return len(s.lower().replace('x', '')) == len(s.lower().replace('o', ''))

print(xo('xo'))

#############大佬的最佳实践
# def xo(s):
#     s = s.lower()
#     return s.count('x') == s.count('o')