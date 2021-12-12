"""
1) Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения
расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""


def zp(hour, rate, premium):
    try:
        denyuzhka = hour * rate + premium
        return denyuzhka
    except ValueError:
        print("Невалидные входные данные")


zarplata = zp(160, 100, 1000)
print(f"{zarplata} рублей Ваша ЗП")

"""
2)Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
"""

Speesok_1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
Speesok_2 = []
for i, el in enumerate(Speesok_1):
    if i == 0:
        continue
    if Speesok_1[i - 1] < Speesok_1[i]:
        Speesok_2.append(Speesok_1[i])

print(Speesok_2)

"""
3) Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
"""

print([i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0])

"""
4)Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел,
соответствующих требованию. Элементы вывести в порядке их следования в исходном списке. Для выполнения задания
обязательно использовать генератор.
"""

# Неправильно понял задачу и искал повторяющиеся элименты и выводил их в единичном варианте в порядке следования.
# Заметил это уже в самом конце ¯\_(ツ)_/¯ Сам себе усложнил задачу, но думаю основную суть выполнил))

a = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
b = []
c = []
e = []
for j in range(min(a), max(a) + 1):
    b.append([i for i, el in enumerate(a) if el == j])
    d = b[0]  # Как избежать того, что внутри переменной "b" параметры добавляються в ещё один список?
    if len(d) >= 2:
        c = d.pop(0)
        e.append(c)
    b = []
g = []
for i, el in enumerate(a):
    for j, al in enumerate(e):
        if i == al:
            g.append(el)
        else:
            continue

print(g)

"""
5) Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить результат
вычисления произведения всех элементов списка. Подсказка: использовать функцию reduce().
"""

from functools import reduce  # Подсмотрел в интернете способ вызова функции reduce() в 3 версии, однако это очень

# похоже на занятие в 4 уроке как импортировать напеисанные нами функции, только тут
# не из дериктории а из функции

items = [i for i in range(100, 1000, 2)]
sum_all = reduce(lambda x, y: x * y, items)  # Эта часть уже плохо понятна как работает (её тоже подсмотрел¯\_(ツ)_/¯)
print(sum_all)

"""
6)Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый
цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""

from itertools import islice, count, cycle  # Пайчарм ругаеться и подчёркивает жёлтой линией "from"
# из-за того что импорт функции стоит не всамом начале?

for i in islice(count(100, 2), 6):
    print(i)

a = ["        *  *  * ", "", "Rastsvetali yabloni i grushi", "Poplyli tumany nad rekoy", "Vykhodila na bereg Katyusha",
     "Na vysokiy bereg na krutoy", "Vykhodila na bereg Katyusha", "Na vysokiy bereg na krutoy", "", "        *  *  * "]

for i in islice(cycle(a), 10):
    print(i)

"""
7) Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. 
При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом:
for el in fact(n). Функция отвечает за получение факториала числа, а в цикле необходимо выводить только
первые n чисел, начиная с 1! и до n!. Подсказка: факториал числа n — произведение чисел от 1 до n.
Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""


def fact(n):
    from itertools import islice, count
    x = 1
    for i in islice(count(1), n + 1):
        x = x * i
        yield x


for el in fact(10):
    print(el)