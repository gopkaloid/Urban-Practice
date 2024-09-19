immutable_var = 13, 22, 34, 55
print(immutable_var)
#immutable_var[2] = 21 #Ошибка при изменении элемента кортежа произошла потому что кортеж не поддерживает обращения по элементам. Элементы кортежа можно изменять только в случае если кортеж содержит в себе изменяемый список.
mutable_list = ["GYM", "Hockey", "Boxing", "Motocross"]
print(mutable_list)
mutable_list[2] = "NBA"
mutable_list.remove("Motocross")
print(mutable_list)
