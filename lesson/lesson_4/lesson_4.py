"""
1) Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения
расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

#
# def zp(hour, rate, premium):
#     try:
#         denyuzhka = hour * rate + premium
#         return denyuzhka
#     except ValueError:
#         print("Невалидные входные данные")
#
#
# zarplata = zp(160, 100, 1000)
# print(f"{zarplata} рублей Ваша ЗП")


"""
2)Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
"""

# Speesok_1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# Speesok_2 = []
# for i, el in enumerate(Speesok_1):
#     if i == 0:
#         continue
#     if Speesok_1[i - 1] < Speesok_1[i]:
#         Speesok_2.append(Speesok_1[i])
#
# print(Speesok_2)

"""
3) Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
"""

# print([i for i in range(20, 240) if i % 20 == 0 or i % 21 == 0])


"""
4)Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел,
соответствующих требованию. Элементы вывести в порядке их следования в исходном списке. Для выполнения задания
обязательно использовать генератор.
"""

# Неправильно понял задачу и искал повторяющиеся элименты и выводил их в единичном варианте в порядке следования.
# Заметил это уже в самом конце ¯\_(ツ)_/¯ Сам себе усложнил задачу, но думаю основную суть выполнил))

# a = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# b = []
# c = []
# e = []
# for j in range(min(a), max(a)+1):
#     b.append([i for i, el in enumerate(a) if el == j])
#     d = b[0]            # Как избежать того, что внутри переменной "b" параметры добавляються в ещё один список?
#     if len(d) >= 2:
#         c = d.pop(0)
#         e.append(c)
#     b = []
# g = []
# for i, el in enumerate(a):
#     for j, al in enumerate(e):
#         if i == al:
#             g.append(el)
#         else:
#             continue
#
# print(g)