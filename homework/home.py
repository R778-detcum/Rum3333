#1  задача
# c = float(input("Введите °C: "))
# f = (9/5) * c + 32
# print(f"{c}°C = {f}°F")

# 2 задача
# age = int(input("Сколько вам лет? "))
#
# if age < 18:
#     print("Молодой")
# elif age <= 60:
#     print("Взрослый")
# else:
#     print("Пожилой")

#3 задача
# number = int(input("Введите число: "))
#
# if number % 3 == 0 and number % 5 == 0:
#     print("Число делится и на 3, и на 5")
# else:
#     print("Число не делится и на 3, и на 5 одновременно")

#4 задача
# number = int(input("Введите число: "))
#
# if number % 7 == 0 and number % 5 != 0:
#     print("число делится на 7, но не делится на 5")
# else:
#     print("условие не выполнено")

#5 задача
# number = int(input("Введите число: "))
#
# print(number)
#
# for i in range(1, number + 1):
#     if i % 3 != 0:
#         print(i)

# 6 задача
# for number in range(1, 101):
#     if number % 2 == 0:
#         print(number)
#     if number > 50:
#         print("Достигли 50")
#         break

#7 задача
# for number in range(1, 11):
#     if number == 6:
#         continue
#     print(number)

#8 задача
# us = int(input("Введите число от 1 до 20: "))
#
# for x in range(1, 21):
#     print(x)
#     if x == us:
#         print(f"Встретили число {us}, остановка!")
#         break

#9 задача
# number = int(input("Введите число: "))
# sum = 0
# k = 1
#
# while k <= number:
#     sum = sum + k
#     k = k + 1
# print(f"Сумма всех чисел от 1 до {number} = {sum}")

#10 задача
# number = int(input("Введите число: "))
# count = 0
# temp = number
# while temp != 0:
#     count = count + 1
#     temp = temp // 10
# print(f"В числе {number} - {count} цифр(ы)")

#11 задача
# number = 2
# sum = 0
# while number <= 100:
#     sum = sum + number
#     number = number + 2
# print(sum)

#12 задача
# number = 10
# print("Обратный отсчет:")
# while number >= 1:
#     print(number)
#     number = number - 1

# 13 задача
# max_number = 0
# print("Вводите числа (0 - для остановки):")
# while True:
#     number = int(input("Введите число: "))
#     if number == 0:
#         break
#     if number > max_number:
#         max_number = number
# print(f"Максимальное введенное число: {max_number}")

#14 задача
# numbers = [5, 16, 67, 29, 8, 21, 11,2]
# count = 0
# i = 0
# while i < len(numbers):
#     if numbers[i] > 10:
#         count = count + 1
#     i = i + 1
# print(f"В списке {numbers}")
# print(f"Количество чисел больше 10: {count}")

#15 задача
# while True:
#     number = int(input("Введите число: "))
#     if number == 0:
#         print("Введен 0, программа завершена")
#         break
#     print(number)

#16 задача
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] список нужен больше
# numbers=list(range(1,31))
# for x in numbers:
#     if x % 3 == 0 and x % 5 == 0:
#         print(x)

#17 задача
# for x in range (1,101):
#     if x % 3 == 0 and x % 5 == 0 :
#         continue
#     print(x)

