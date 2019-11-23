import math                           #math.ceil()
def isint(n):
    return int(n) != float(n)
all_square = float(input('Введите общую площадь: '))
s_detal_1 = float(input('Введите площадь 1 детали: '))
cost_detal_1 = float(input('Введите стоимость 1 детали: '))
s_detal_2 = float(input('Введите площадь 2 детали: '))
cost_detal_2 = float(input('Введите стоимость 2 детали: '))
s_detal_3 = float(input('Введите площадь 3 детали: '))
cost_detal_3 = float(input('Введите стоимость 3 детали: '))
value1 = all_square / s_detal_1 * cost_detal_1
kolvo1 = all_square / s_detal_1
value2 = all_square / s_detal_2 * cost_detal_2
kolvo2 = all_square / s_detal_2
value3 = all_square / s_detal_3 * cost_detal_3
kolvo3 = all_square / s_detal_3
if value1 > value2 and value1 > value3:
    value1 = round(value1, 2)
    if isint(kolvo1):
        kolvo1 = math.ceil(kolvo1)
    print('Суммарная стоимость: ',value1,'\n','Количество деталей 1 вида: ',kolvo1)
elif value2 > value3 and value2 > value1:
    if isint(kolvo2):
        kolvo2 = math.ceil(kolvo2)
    value2 = round(value2, 2)
    print('Суммарная стоимость: ',value2,'\n','Количество деталей 2 вида: ',kolvo2)
elif value3 > value1 and value3 > value2:
    if isint(kolvo3):
        kolvo3 = math.ceil(kolvo3)
    value3 = round(value3, 2)
    print('Суммарная стоимость: ',value3,'\n','Количество деталей 3 вида: ',kolvo3)
if value1 == value2 == value3:
    value1 = round(value1, 2)
    if isint(kolvo1):
        kolvo1 = math.ceil(kolvo1)
    print('Суммарная стоимость: ', value1, '\n', 'Количество деталей: ', kolvo1)
