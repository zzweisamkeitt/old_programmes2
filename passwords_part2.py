class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


class SequenceError(PasswordError):
    pass


dangerous_combinations = ['йцу', 'цук', 'уке', 'кен', 'енг', 'нгш', 'гшщ', 'шщз', 'щзх', 'жэё',
                          'зхъ', 'фыв', 'ыва', 'вап', 'апр', 'про', 'рол', 'олд', 'лдж', 'джэ',
                          'ячс', 'чсм', 'сми', 'мит', 'ить', 'тьб', 'ьбю', 'qwe', 'wer', 'ert',
                          'rty', 'tyu', 'yui', 'uio', 'iop', 'asd', 'sdf', 'dfg', 'fgh', 'ghj',
                          'hjk', 'jkl', 'zxc', 'xcv', 'cvb', 'vbn', 'bnm']


def check_password(password):
    global dangerous_combinations
    if len(password) > 8:
        n = 0
        if not password.isdigit():
            for elem in list(password):
                if elem.isdigit():
                    n += 1
            if n != 0:
                if password.upper() != password:
                    if password.lower() != password:
                        for element in dangerous_combinations:
                            if element in password.lower():
                                raise SequenceError
                    else:
                        raise LetterError
                else:
                    raise LetterError
            else:
                raise DigitError
        else:
            raise LetterError
    else:
        raise LengthError
    return 'ok'
