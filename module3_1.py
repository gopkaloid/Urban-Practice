def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    length = len(string)
    uppercase = string.upper()
    lowercase = string.lower()
    return length, uppercase, lowercase

def is_contains(string, list_to_search):
    count_calls()
    search_list = [item.lower() for item in list_to_search]
    if string.lower() in search_list:
        return True
    else:
        return False

calls = 0

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)