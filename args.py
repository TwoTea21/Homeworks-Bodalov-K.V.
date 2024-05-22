def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(10)
print_params(78, 101, 'i hate c++')
print_params(b=25)
print_params(c=[1, 2, 3])


values_list = [True, 'Fallout', '34']
values_dict = {'a': 4, 'b': 9, 'c': 25}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['obsidian', 2005, False]

# print_params(*values_list_2, 42) не работает, слишком много элементов
print_params(*values_list_2[0:1], 42)  # так работает, но мы потеряли 2005
