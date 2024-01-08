####Task-1
# Напишіть функцію, яка обчислює добуток елементів списку цілих.
# Список передається як параметр.
# Отриманий результат повертається із функції.

# def calculate_product(lst):
#     if not lst:
#         return 0
#     from functools import reduce
#     product = reduce(lambda x, y: x * y, lst)
#     return product
# my_list = [2, 3, 5, 7]
# result_product = calculate_product(my_list)
# print("Product of the list {}: {}".format(my_list, result_product))

####Task-2
# Напишіть функцію для знаходження мінімуму у списку цілих.
# Список передається як параметр.
# Отриманий результат повертається із функції.

# def find_minimum(lst):
#     if not lst:
#         return None
#     return min(lst)
# my_list = [4, 1, -3, 3, 0]
# result_minimum = find_minimum(my_list)
# print("Minimum value in the list {}: {}".format(my_list, result_minimum))

####Task-3
# Напишіть функцію, яка визначає кількість простих чисел у списку цілих.
# Список передається як параметр.
# Отриманий результат повертається із функції

# def count_primes(numbers):
#     def is_prime(n):
#         return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
#     return sum(1 for number in numbers if is_prime(number))
# my_numbers = [2, 3, 5, 7, 8, 11, 13, 16, 17, 19, 23]
# result = count_primes(my_numbers)
# print("Number of prime numbers in the list {}: {}".format(my_numbers, result))

####Task-4
# Напишіть функцію, яка видаляє зі списку ціле задане число.
# З функції потрібно повернути кількість видаленних елементів.

# def remove_integer(lst, target):
#     deleted_count = lst.count(target)
#     lst = [item for item in lst if item != target]
#     return deleted_count
# my_list = [1, 2, 3, 4, 2, 5, 2, 3]
# target_number = 3
# deleted_count = remove_integer(my_list, target_number)
# print("List after removing {}: {}".format(target_number, my_list))
# print("Number of deleted items: {}".format(deleted_count))

####Task-5
# Напишіть функцію, яка отримує два списки як параметр і повертає список,
# що містить елементи обох списків.

# def combine_lists(list1, list2):
#     return list1 + list2
# first_list = [8, 5, 2]
# second_list = [3, 7, 5]
# result_list = combine_lists(first_list, second_list)
# print("Combined list: {}".format(result_list))

####Task-6
# Напишіть функцію, яка обчислює ступінь кожного елемента списку цілих.
# Значення для ступеня передається як параметр, список також передається як параметр.
# Функція повертає новий список, який містить отримані результати.

# def calculate_degree(numbers, degree):
#     result_list = [number ** degree for number in numbers]
#     return result_list
# input_list = [3, 2, 5]
# degree_value = 3
# result_degrees = calculate_degree(input_list, degree_value)
# print("List after calculating {}-degree: {}".format(degree_value, result_degrees))


