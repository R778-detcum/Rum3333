#1 задание
# str1 = input("Введите первую строку: ")
# str2= input ("Введите вторую строку: ")
# if str1==str2:
#     print("строки равны")
# else :
#     len1 = len(str1)
#     len2 = len(str2)
#     if len1 > len2:
#         difference = len1 - len2
#         print(f"первая строка длиннее на {difference} символов")
#     elif len1<len2 :
#         difference = len2 - len1
#         print(f"вторая строка длиннее на {difference} символов")
#     else :
#         print(f"строки имеют одинаковую длину , но по символам не равны")

# 2 задание

# user_input = input("Введите строку: ")
#
#
# cleaned_string = user_input.strip()
#
# words_list = cleaned_string.split()
#
# word_count = len(words_list)
# print(f"Количество слов в строке: {word_count}")
#
# upper_case = cleaned_string.upper()
# print(f"Строка в верхнем регистре: {upper_case}")
#
# replaced_string = cleaned_string.replace("кот", "собака")
# print(f"После замены: {replaced_string}")
#
# joined_string = ", ".join(words_list)
# print(f"Слова через запятые: {joined_string}")

# 3 задание
# word = input ("введите слово")
# vowels = 'aeiouAEIOU'
#
#
# for char in word :
#     if char in vowels :
#
#         print(f'{char} - гласный символ')
#     else:
#         print(f'{char}-символ согласный' )
# 4 задание

# user_input = input("Введите строку: ")
#
# words = user_input.split()
#
# palindromes = []
#
# for word in words:
#     if word.lower() == word.lower()[::-1]:
#         palindromes.append(word)
#
# if palindromes:
#     print(f"Найдены палиндромы: {palindromes}")
# else:
#     print("В строке нет палиндромов")



# 5 задание

# user_string = input("Введите строку: ")
#
# total_sum = 0
#
# for char in user_string:
#       if char.isdigit():
#         total_sum += int(char)
# print(f"Сумма всех цифр в строке: {total_sum}")