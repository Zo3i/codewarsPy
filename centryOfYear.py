def century(year):
    return year // 100 if year % 100 == 0 else year // 100 + 1 
print(century(1910))

######大佬的最佳实践
def century(year):
return (year + 99) // 100