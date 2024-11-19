my_dict = {'Dmitry': 1987, 'Mama': 1960, 'Papa': 1955}
print(my_dict)
print(my_dict.get('Mama'))
print(my_dict.get('Lena'))
my_dict['Sestra'] = 1984
my_dict.update({'Brat': 1986})
del my_dict['Dmitry']
print(my_dict.get('Dmitry'))
print(my_dict)
my_set = {1, 1, 2, 2, 'set', 'get', 5, 'set'}
print(my_set)
my_set.add(3)
my_set.add(4)
my_set.discard('set')
print(my_set)