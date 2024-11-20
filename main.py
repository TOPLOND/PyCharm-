# Модуль 4/1 - 1
# def display_quote():
#     print('“Don\'t compare yourself with anyone in this world…')
#     print('if you do so, you are insulting yourself.”')
#     print('Bill Gates')
#
# display_quote()

# Модуль 4/1 - 2
# def display_even_numbers(start, end):
#     for num in range(start, end + 1):
#         if num % 2 == 0:
#             print(num)
#
# display_even_numbers(10, 20)

# Модуль 4/1 - 3
# def draw_square(side_length, symbol, filled):
#     if filled:
#         for _ in range(side_length):
#             print(symbol * side_length)
#     else:
#         print(symbol * side_length)
#         for _ in range(side_length - 2):
#             print(symbol + ' ' * (side_length - 2) + symbol)
#         print(symbol * side_length)
#
# draw_square(5, '*', True)
# draw_square(5, '*', False)

# Модуль 4/1 - 4
# def find_min(a, b, c, d, e):
#     return min(a, b, c, d, e)
#
# print(find_min(11, 5, 8, 6, 7))

# Модуль 4/1 - 5
# def product_in_range(start, end):
#     if start > end:
#         start, end = end, start
#     product = 1
#     for num in range(start, end + 1):
#         product *= num
#     return product
#
# print(product_in_range(5, 2))

# Модуль 4/1 - 6
# def count_digits(number):
#     return len(str(abs(number)))
#
# print(count_digits(356))

# Модуль 4/1 - 7
# def is_palindrome(number):
#     str_num = str(number)
#     return str_num == str_num[::-1]
#
# print(is_palindrome(123321))
# print(is_palindrome(421987))