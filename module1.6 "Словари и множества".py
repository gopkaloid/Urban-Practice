my_dict = {'Luke' : 1996, 'Vlad' : 1994, 'Igor' :1996, 'Kate' :2001}
print(my_dict)
print(my_dict ['Vlad'])
print(my_dict.get('Nikita'))
my_dict.update({'Irina' : 2003,
                'Pavel' : 1987})
del my_dict ['Kate']
print(my_dict)


my_set = {10, 15, 10, 20, 15, 10, 20, 15, 10, 20, 20, 5, 5, 5 ,10, 'Apple', False, 'Apple'}
print(my_set)
my_set.update([25, 30])
my_set.discard(False)
print(my_set)