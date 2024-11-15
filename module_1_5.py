immutable_var = 1, 2, 3, 'a', 'b', 'c'
print(type(immutable_var))
print(immutable_var)
#immutable_var [0] = 5
#print(immutable_var) # нельзя менять так так кортеж не поддерживает обращение по элементам
mutable_list = [1, 2, 3, 'a', 'b', 'c']
mutable_list.append('d')
mutable_list[1]= 3
print(mutable_list)