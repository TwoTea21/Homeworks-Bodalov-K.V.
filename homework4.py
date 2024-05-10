immutable_var = 12, 'Oleg', False, 3.14
print('Immutable tuple:', immutable_var)
#Кортеж является неизменяемым ( то есть его объекты не являются изменяемыми). Но к кортежу можно добавить ещё объекты
#сложением и умножением.
mutable_list = ['boom','bap','pam-pam']
mutable_list[0] = 'bang'
print('Mutable list:', mutable_list)

