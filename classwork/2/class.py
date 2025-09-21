#1 задача
# lskh=list(range(1,21))
# print(lskh)

#2 задача
# numbers=[1,2,3,4,5]
# total_sum=sum(numbers)
# total_product=1
# for num in numbers:
#     total_product*= num
# print(f"Cумма: {total_sum}")
# print(f"Произведение: {total_product}")

# 3 задача
# numb= [1,2,3,4,5,6,7]
# chetni=[]
#
# for num in numb:
#     if num % 2 == 0 :
#         chetni.append(num)
# print(chetni)

#4 задача
# n= int(input("Введите число: "))
# numbers = range (1, n+1)
# for x in numbers:
#     if x%3==0 :
#         print(x)

#5 задача
# numbers = [1,2,3,4,5,6,7,8,9]
# minimum = numbers [0]
# maximum = numbers [0]
# for x in numbers:
#     if x < minimum :
#         minimum = x
#     if x > maximum :
#          maximum = x
# print("Минимальный элемент:", minimum)
# print("Максимальный элемент:",maximum)

#6 задача
# spisok= [1,2,2,3,3,4,5,6,6]
#
# x = len(set(spisok))
# print(x)

#7 задача
# numbers = [1,-2,3,-4,5]
# for x in range (len(numbers)):
#     if numbers[x]<0 :
#         numbers[x]= 0
# print(numbers)

#8 задача
# numbers = [2,10,13,56,2,3,4,-1]
# min_index= max_index=0
# for i, num in enumerate(numbers):
#     if num < numbers[min_index]:
#         min_index= i
#     if num > numbers [max_index]:
#         max_index= i
# numbers[min_index], numbers[max_index]=numbers[max_index], numbers[min_index]
# print(numbers)

#9 задача
# numbers= sorted([5,12,7,3,-2,20,10])
# print(numbers)

#10 задача
# x= [1,2,3]
# y=[4,5,6]
# x.extend(y)
# print(x)

#11 задача
# spisok= [ 2,50,55,75,67]
# for x in spisok:
#     if x>50 :
#      print(x)

#12 задача
# chisla = [1,2,3,4,5]
# x= [num**2 for num in chisla]
# print(x)

#13 задача
# numbers=[1,2,3,4,5,6,7,8,9,10]
# new= []
# for x in numbers :
#     if x % 2 == 0 :
#         new.append(x)
#     else :
#         new.append(x)
# print(new)
#14 задача
# numbers = [3,7,2,5,10]
# ar= sum(numbers)/len(numbers)
# new=[]
#
# for x in numbers:
#     if x<ar:
#         new.append(-1)
#     else :
#         new.append(x)
# print(new)