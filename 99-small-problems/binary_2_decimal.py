
def binary_2_decimal(s):
    exponent = 0
    total = 0
    for i in range(len(s)-1, -1, -1):
        if s[i] == '1':
            total += 2 ** exponent
        exponent += 1
    return total


print(binary_2_decimal("1001101"))