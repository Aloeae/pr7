print('Введите целое положительное десятчное число: ')
number=input()
if number.isdigit():
    bin_n=bin(int(number))
    print(f'Число {number} в двоичной состеме счисления: {bin_n[2:]};')
    oct_n=oct(int(number))
    print(f'Число {number} в восьмиричной состеме счисления: {oct_n[2:]}.')
else:
    print('Ошибка! Введите целое десятичное число.')
