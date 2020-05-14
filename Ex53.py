def vatcal(total):
    result = total+(total*7/100)
    return result
print(vatcal(int(input())))