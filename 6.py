def mul02(num):
    a = (num >> 7) * 0b00011011
    result = (num << 1) ^ a
    return result & 0b11111111


def mul03(num):
    return mul02(num) ^ num


print('D4 * 02 =', format(mul02(int('D4', 16)), 'x').upper())
print('BF * 03 =', format(mul03(int('BF', 16)), 'x').upper())

# Контрольна робота В16 перевірка
#print('1A * 02 =', format(mul02(int('1A', 16)), 'x').upper())
#print('77 * 03 =', format(mul03(int('77', 16)), 'x').upper())
