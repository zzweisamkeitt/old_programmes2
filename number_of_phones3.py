class Error(Exception):
    pass


class CountOfBrackets(Error):
    pass


class ConsecutiveSigns(Error):
    pass


class WrongSignLocation(Error):
    pass


incoming_data = input().split()
number = []
for elem in incoming_data:
    for element in list(elem):
        number.append(element)

try:
    if number[0] == '8' or (number[0] == '+' and number[1] == '7'):
        if number.count('(') == number.count(')'):
            for i in range(len(number) - 1):
                if number[i] == number[i + 1] == '(':
                    raise ConsecutiveSigns
            for j in range(len(number) - 1):
                if number[j] == number[j + 1] == ')':
                    raise ConsecutiveSigns
            while '(' in number:
                number.remove('(')
            while ')' in number:
                number.remove(')')
            if '-' in number:
                if number[-1] != '-':
                    if number[0] != '-':
                        for k in range(len(number) - 1):
                            if number[k] == number[k + 1] == '-':
                                raise ConsecutiveSigns
                        while '-' in number:
                            number.remove('-')
                        if number[0] == '8':
                            number.remove('8')
                            number.insert(0, '7')
                            number.insert(0, '+')
                    else:
                        raise WrongSignLocation
                else:
                    raise WrongSignLocation
            else:
                if number[0] == '8':
                    number.remove('8')
                    number.insert(0, '7')
                    number.insert(0, '+')
        else:
            raise CountOfBrackets
    else:
        raise Error
    if len(number) == 12:
        for elem in number:
            print(elem, end='')
    else:
        print('неверное количество цифр')
except Error:
    print('неверный формат')
