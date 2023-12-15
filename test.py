import sys
class romanNumber:
    """Класс реализующий представление римских цифр

        Позволяет переводить из целого римского цисла
        в русское (арабское) и обратно,
        производить над числами арифметические операции

        ...

        Attributes
        --------
        roman_squad_2 : dict
            Словарь римских цифр с
            их десятичными значениями
        roman_squad : list
            Словарь кортежей,
            в каждом таком содержащий
            десятичную и римскую запись
            числа

        Methods
        --------
        convert_to_roman(converting_num):
            представляет десятичное
            число в виде римского

        convert_from_roman(converting_num):
            представляет римское число
            в виде десятичного





    """
    roman_squad_2 = {'M': 1000,
                     'CM': 900,
                     'D': 500,
                     'CD': 400,
                     'C': 100,
                     'XC': 90,
                     'L': 50,
                     'XL': 40,
                     'X': 10,
                     'IX': 9,
                     'V': 5,
                     'IV': 4,
                     'I': 1
                     }

    roman_squad = [(1000, 'M'),
                   (900, 'CM'),
                   (500, 'D'),
                   (400, 'CD'),
                   (100, 'C'),
                   (90, 'XC'),
                   (50, 'L'),
                   (40, 'XL'),
                   (10, 'X'),
                   (9, 'IX'),
                   (5, 'V'),
                   (4, 'IV'),
                   (1, 'I')]

    def __init__(self, class_number):
        """инициализируем класс

            в первом if проверяем, десятичное или
            римское число ввел пользователь
            мы по-разному их присваиваем
            разные типы
            переменной roman_value

            Args:
            --------
            class_number : str/int
                величина нашего числа(или
                в обычной, или
                в римской форме записи)


            >>
        """

        if type(class_number) == int or class_number.isdigit():
            self.roman_value = self.convert_to_roman(int(class_number))
        else:
            roman_constructor = ''
            for curr_num in class_number:
                roman_constructor += curr_num
            self.roman_value = roman_constructor
    def convert_to_roman(self, converting_num):
        """представляет десятичное
            число в виде римского

            первое условие добавляет минус в запись
            если начальное число отрицательное
            второй цикл переводит число из десятичного
            в римское путем целочисленногно деления,
            размещая в начале самые крупные цифры,
            которые могут вместиться в число

            Args:
            --------
            converting_num : str
                число, которое мы переводим

            Returns:
            --------
            a_signed_number : str
                число в преобразованном виде

            Raises:
            --------
            ValueError

            Examples:
            >> convert_to_roman(123)
            'CXXIII'
                ...
            >> convert_to_roman(gfjja)
            'Нужно ввести число'
        """

        number_sign = ''
        if converting_num < 0:
            number_sign = '-'
            try:
                converting_num = converting_num*-1
            except ValueError:
                print('Нужно ввести число')

        roman_number = ''

        while converting_num > 0:
            for current_symb in self.roman_squad:
                while converting_num // current_symb[0] > 0:
                    roman_number += current_symb[1]
                    converting_num -= current_symb[0]
        a_signed_number = number_sign + roman_number
        return a_signed_number

    def convert_from_roman(self, converting_num):
        """представляет римское число
            в виде десятичного

            первое условие добавляет минус к числу
            если начальное число отрицательное
            второй цикл переводит число из десятичного
            в римское путем целочисленногно деления,
            размещая в начале самые крупные цифры,
            которые могут вместиться в число

            Args:
            --------
            converting_num : str
                число, которое мы переводим

            Returns:
            --------
            a_signed_number : str
                число в преобразованном виде

            Examples:
            >> convert_from_roman('CXXIII')
            123
                ...
            >> convert_from_roman('XII')
            12

        """

        first_symb = converting_num[0]
        sign_multiplier = 1
        if first_symb == '-':
            sign_multiplier = -1
            converting_num = converting_num[1:]
        int_number = 0
        last_unit = ''

        while len(converting_num) > 0:
            last_unit = converting_num[-1]
            conv_len = len(converting_num)
            while (conv_len >= 2 and
                   self.roman_squad_2[converting_num[-1]] > self.roman_squad_2[converting_num[-2]]):
                converting_num = converting_num[:-1]
                last_unit = converting_num[-1] + last_unit
            int_number += self.roman_squad_2[last_unit]
            converting_num = converting_num[:-1]
            last_unit = ''
        a_signed_number = int_number * sign_multiplier
        return a_signed_number

    def __str__(self):
        """Задаем формат вывода
            нашего числа

            Returns:
            --------
            roman_value : str
                выводящееся число
        """
        return self.roman_value

    def __add__(self, other_number):
        """Перегружаем оператор '+'

            Args:
            --------
            other_number : str, int
                класс второго слагаемого

            Returns:
            --------
            roman_result : str
                сумма в преобразованном виде

            Examples:
            --------
            >> a = romanNumber(15)
            >> b = romanNumber(16)
            >> a+b
                'XXXI'
        """

        self_value = self.convert_from_roman(self.roman_value)
        other_value = self.convert_from_roman(other_number.roman_value)
        int_result = self_value + other_value
        roman_result = self.convert_to_roman(int_result)
        return roman_result


    def __sub__(self, other_number):
        """Перегружаем оператор '-'

            Args:
            --------
            other_number : str, int
                класс вычитаемого

            Returns:
            --------
            roman_result : str
                разность в преобразованном виде

            Examples:
            --------
            >> a = romanNumber(15)
            >> b = romanNumber(16)
            >> a-b
                'XXXI'
        """
        self_value = self.convert_from_roman(self.roman_value)
        other_value = self.convert_from_roman(other_number.roman_value)
        int_result = self_value - other_value
        roman_result = self.convert_to_roman(int_result)
        return roman_result

    def __mul__(self, other_number):
        """Перегружаем оператор '*'

            Args:
            --------
            other_number : str, int
                класс второго множителя

            Returns:
            --------
            roman_result : str
                произведение в преобразованном виде

            Examples:
            --------
            >> a = romanNumber(XV)
            >> b = romanNumber(XVI)
            >> a*b
                'CCXL'
        """
        self_value = self.convert_from_roman(self.roman_value)
        other_value = self.convert_from_roman(other_number.roman_value)
        int_result = self_value * other_value
        roman_result = self.convert_to_roman(int_result)
        return roman_result

    def __truediv__(self, other_number):
        """Перегружаем оператор '/'

            Args:
            --------
            other_number : str, int
                класс второго множителя

            Returns:
            --------
            roman_result : str
                произведение в преобразованном виде

            Examples:
            --------
            >> a = romanNumber(XV)
            >> b = romanNumber(XVI)
            >> a/b
                None
                ...

            >> a = romanNumber(XV)
            >> b = romanNumber(V)
            >> a/b
                'III'
        """
        self_value = self.convert_from_roman(self.roman_value)
        other_value = self.convert_from_roman(other_number.roman_value)
        int_result = self_value // other_value
        if self_value % other_value > 0:
            return None
        roman_result = self.convert_to_roman(int_result)
        return roman_result

def check_roman(variable_number):
    """Проверяем, является ли число римским

        В цикле пробегаемся по цифрам и проверяем
        есть ли они среди римских

        Args:
        --------
        variable_number : str
            проверяемое число

        Returns:
        --------
        : bool
            True - римское|False - не римское

        Examples:
        --------
        >> VI
            True
            ...
        >> g
            False
    """
    for current_digit in variable_number:
        if current_digit not in romanNumber.roman_squad_2:
            return False
    return True

def do_function(func_number):

    """Вызываем нужную нам ф-ию в зависимости от
        выбранного пользователем действия

        в каждом case выполняем
        запрошенное пользователем действие

         Args:
        --------
        func_number : int
            номер действия

        Examples:
        --------
            >> введите номер действия:1
                +--------------------------------------------------+
                Введите целое число:
                    ... '1 case has been completed'

            >> введите номер действия:x
                +--------------------------------------------------+

                Process finished with exit code 0

            ...
            >> g
                False
    """

    print('+' + '-' * 50 + '+')
    match func_number:
        case '1':
            try:
                variable_number = input('Введите целое число:')
            except ValueError:
                print('нужно ввести целое число')
            final_number = romanNumber(variable_number)
            print(f'результат = {final_number}')

        case '2':
            while True:
                variable_number = str(input('Введите римское число:'))

                if not check_roman(variable_number):
                    print('Неверно введено число')
                    continue

                roman_object = romanNumber(variable_number)
                converting_function = roman_object.convert_from_roman
                final_number = converting_function(variable_number)
                print(f'результат = {final_number}')
                break

        case '3':
            while True:
                first_roman = input('1-oe римское число:')
                if not check_roman(first_roman):
                    print('Неверно введено число')
                    continue
                second_roman = input('2-oe римское число:')

                if not check_roman(second_roman):
                    print('Неверно введено число')
                    continue

                first_roman = romanNumber(first_roman)
                second_roman = romanNumber(second_roman)
                final_number = first_roman + second_roman
                print(f'результат = {final_number}')
                break
        case '4':
            while True:
                first_roman = input('1-oe римское число:')
                if not check_roman(first_roman):
                    print('Неверно введено число')
                    continue
                second_roman = input('2-oe римское число:')

                if not check_roman(second_roman):
                    print('Неверно введено число')
                    continue

                first_roman = romanNumber(first_roman)
                second_roman = romanNumber(second_roman)
                final_number = first_roman - second_roman
                print(f'результат = {final_number}')
                break
        case '5':
            while True:
                first_roman = input('1-oe римское число:')
                if not check_roman(first_roman):
                    print('Неверно введено число')
                    continue
                second_roman = input('2-oe римское число:')

                if not check_roman(second_roman):
                    print('Неверно введено число')
                    continue

                first_roman = romanNumber(first_roman)
                second_roman = romanNumber(second_roman)
                final_number = first_roman * second_roman
                print(f'результат = {final_number}')
                break
        case '6':
            while True:
                first_roman = input('1-oe римское число:')
                if not check_roman(first_roman):
                    print('Неверно введено число')
                    continue
                second_roman = input('2-oe римское число:')

                if not check_roman(second_roman):
                    print('Неверно введено число')
                    continue

                first_roman = romanNumber(first_roman)
                second_roman = romanNumber(second_roman)
                final_number = first_roman / second_roman
                if final_number == None:
                    final_number = 'Не делится нацело'
                print(f'результат = {final_number}')
                break
        case 'x':
            sys.exit(0)
        case _:
            print('Опции с таким номером нет')

while True:
    print('+' + '-' * 24 + 'menu'  + 24*'-' + '+')
    print('[1] - перевести целое русское (арабское) цисло в римское')
    print('[2] - перевести целое римское цисло в русское (арабское)')
    print('[3] - сложить два римских числа и представить в виде римского')
    print('[4] - отнять от одного числа другое и представить в виде римского')
    print('[5] - умножить два римских числа и представить в виде римского')
    print('[6] - поделить одно число на другое и представить в виде римского')
    print('[x] - выйти')

    menu_action = input('введите номер действия:')

    do_function(menu_action)
