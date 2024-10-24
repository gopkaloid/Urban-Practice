def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(a = 0)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = ['строка', False, 42]
values_dict = {'a': 'строка', 'b': False, 'c': 42}

def print_params(a, b, c):
    print(a, b, c)

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']

def print_params(a, b, c):
    print(a, b, c)

print_params(*values_list_2, 42)