def get_multiplied_digits(number):
    str_number = str(number)
    if len(str_number) <= 1:
        return int(str_number)

    first = int(str_number[0])
    rest = int(str_number[1:])
    result = first * get_multiplied_digits(rest)
    return result

result = get_multiplied_digits(40203)
print(result)