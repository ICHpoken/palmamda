import math                           #math.ceil()
def isInt(n):
    return int(n) != float(n)
amount = 0
final_value = 0
all_square = float(input('Введите общую площадь: '))
kinds = int(input('Введите количесвто видов деталей: '))
for i in range(kinds):
    print('Введите характеристики для детали', i + 1,'вида')
    s_detal = float(input('Площадь: ' ))
    cost_detal = float(input('Стоимость: '))
    value = all_square / s_detal * cost_detal
    kolvo = all_square / s_detal
    if value > final_value:
        final_value = round(value, 2)
        amount = math.ceil(kolvo)
        kind = i + 1
print('Суммарная стоимость: ',final_value,'\n','Количество деталей',kind,'вида: ',amount)