def convert(number):
    if number < 13:
        return str(number)
    else:
        return convert(number // 13) + str(number % 13)

number_in = input("Введите десятичное целое положительное число: ")

if number_in.isdigit():
    number1 = int(number_in)
    print(f"Результат(тринадцатеричная система счисления): {convert(number1)}")
else:
    print("Ошибка! Для реализации программы необходимо ввести целое положительное число.")
