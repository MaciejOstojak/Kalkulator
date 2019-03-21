def calc_add(*args):
    print(args)
    list_args = list(args[0].strip(' ').split(' ')
    return sum([int(i) for i in list_args])



def calc_substract(a, b):
    print('{} + {} ='.format(str(a), str(b)), end=' ')
    return a - b

def calc_multiple(a, b, *args):
    print('{} + {} ='.format(str(a), str(b)), end=' ')
    return a * b

def calc_divide(a, b):
    print('{} + {} ='.format(str(a), str(b)), end=' ')
    try:
        return a / b
    except ZeroDivisionError:
        print('Nie dzielimy przez zero!')

def check_operation_name(operation):
        if operation in method_dict:
            return method_dict[operation] 
        operation = input('Niepoprawne dzialanie, podaj jeszcze raz: dodawanie, odejmowanie, mnozenie, dzielenie: ')
        check_operation_name(operation)

method_dict = {
    'dodawanie': calc_add,
    'odejmowanie': calc_substract,
    'mnozenie': calc_multiple,
    'dzielenie': calc_divide
}

if __name__ == "__main__":
    print('Witam w moim kalkulatorze :D')
    while True:
        operation = input('Podaj dzialanie: dodawanie, odejmowanie, mnozenie, dzielenie: ')
        if operation == 'exit':
            break

        operation_def = check_operation_name(operation)
        a = int(input('Podaj pierwsza liczbe:'))
        b = int(input('Podaj druga liczbe:'))
        print(operation_def(a, b))

















































