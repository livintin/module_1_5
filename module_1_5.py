immutable_var = ('name', 1, True, 1.2)
print(immutable_var)
immutable_var[0] = 'firstname' #объект "кортеж" не поддерживает назначение(изменение) элементов
mutable_list = ['yang', 1, 1.2, False]
mutable_list[0] = 'old'
print(mutable_list)
