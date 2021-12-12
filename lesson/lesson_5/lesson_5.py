"""
1) Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об
окончании ввода данных свидетельствует пустая строка.
"""

# new_fail = open('test.txt', 'a')
# a = input('Введите текст: ')
# while a:
#     new_fail.writelines(a + '\n')
#     a = input('Введите текст: ')
#     if not a:
#         new_fail.close()
#         break
#
# """
# 2) Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.
# """
#
# with open("test.txt", "r") as file:
#     file_lines = file.readlines()
#     print("Количество строк в файле: ", len(file_lines))
#     for line_number, line in enumerate(file_lines, 1):
#         print(f"Количество слов в строке {line_number}:", len(line.split()))


"""
3) Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

# vsego = 0
#
# with open("test_2.txt") as file:
#     lines = file.readlines()
#     for line in lines:
#         surname, zp = line.split()
#         vsego += int(zp)
#         if int(zp) < 20000:
#             print("Имеет оклад менее 20 тыс.:", surname)
#
# print("Среднеяя величина дохода сотрудников:", vsego/len(lines))


"""
4) Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""


# translate_dict = {"One": "Один",
#                   "Two": "Два",
#                   "Three": "Три",
#                   "Four": "Четыре",
#                   "Five": "Пять",
#                   "Six": "Шесть",
#                   "Seven": "Семь"}
#
# with open("test_3", "r") as file_read, open("test_4", "w") as file_write:
#     for line in file_read.readlines():
#         text_number, number = line.rstrip().split(' - ')
#         file_write.write(f'{translate_dict[text_number]} - {number}\n')


"""
5) Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open("File5", "w") as file_w:
    input_numbers = input("Введите числа через пробел: ")
    print(input_numbers, file=file_w)

with open("File5") as file:
    content_list = file.read().rstrip().split()
    print(content_list)
    numbers_list = [int(number) for number in content_list if number.isdigit()]
    print(numbers_list)
    print(sum(numbers_list))
