def sum_of_digits(n):
    """Функция для вычисления суммы цифр числа."""
    return sum(int(digit) for digit in str(abs(n)))

def main():
    max_sum = -1  # Переменная для хранения максимальной суммы цифр
    number_with_max_sum = None  # Число с максимальной суммой цифр

    while True:
        try:
            user_input = int(input("Введите целое число (0 для выхода): "))
        except ValueError:
            print("Пожалуйста, введите целое число.")
            continue

        if user_input == 0:
            break  # Выход из цикла, если введен 0

        # Вычисляем сумму цифр текущего числа
        current_sum = sum_of_digits(user_input)

        # Проверяем, является ли текущая сумма цифр максимальной
        if current_sum > max_sum:
            max_sum = current_sum
            number_with_max_sum = user_input

    if number_with_max_sum is not None:
        print(f"Число с максимальной суммой цифр: {number_with_max_sum} (сумма цифр: {max_sum})")
    else:
        print("Не было введено ни одного числа.")

if __name__ == "__main__":
    main()
