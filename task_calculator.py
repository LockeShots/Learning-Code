def calc_str(text, previous):
    """
    >>> calc_str('1 + 1', None)
    2.0
    >>> calc_str('2 * 3', None)
    6.0
    >>> calc_str('18 % 4', None)
    2.0
    >>> calc_str('1.5 + 1.5', None)
    3.0
    >>> calc_str('2 / 3', None)
    0.667
    >>> calc_str('+ 2', 2)
    4.0
    
    #>>> calc_str('')
    ?
    #>>> calc_str('bob is cool')
    #ValueError:
    """

    items = text.split()
    if len(items) == 2:
        number1 = float(previous)
        operator = items[0]
        number2 = float(items[1])
    else:
        number1 = float(items[0])
        operator = items[1]
        number2 = float(items[2])

    answer = None

    #aa = {'0':'bob', "1":'jane', "2":'sally'}
    #aa["1"]
    import operator
    ops = {
        '+': operator.add,
        '*': operator.mul,
        #'plus': operator.add,
    }
    #alias = (
    #    (operator.add, ('plus', 'PLUS', 'pp', '+'))
    #)
    answer = ops[operator](number1, number2)
    #if (operator == '+'):
    #    answer = number1 + number2
    #if (operator == '*'):
    #    answer = number1 * number2
    #if (operator == '%'):
    #    answer = number1 % number2
    #if (operator == '/'):
    #    answer = number1 / number2
    return round(answer, 3)


if __name__ == '__main__':
    previous = None
    while True:
        text = input('>>> ')
        answer = calc_str(text, previous)
        previous = answer
        print(answer)