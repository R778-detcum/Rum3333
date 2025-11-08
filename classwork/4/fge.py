#1
numbers = [5, 2, 8, 2, 5, 1, 8, 8, 3]
print("Исходный список:", numbers)
unique_numbers = set(numbers)
print("Множество уникальных элементов:", unique_numbers)
count_unique = len(unique_numbers)
print("Количество уникальных элементов:", count_unique)
#2
# Задача 2

vasyas_movies = ["Матрица", "Начало", "Матрица", "Интерстеллар"]
petas_movies = ["Начало", "Аватар", "Интерстеллар", "Титаник"]

print("Фильмы Васи:", vasyas_movies)
print("Фильмы Пети:", petas_movies)

vasyas_set = set(vasyas_movies)
petas_set = set(petas_movies)
print("Уникальные фильмы Васи:", vasyas_set)
print("Уникальные фильмы Пети:", petas_set)
common_movies = vasyas_set.intersection(petas_set)
print("Общие фильмы (intersection):", common_movies)
#3
vasyas_movies = ["Матрица", "Начало", "Матрица", "Интерстеллар"]
petas_movies = ["Начало", "Аватар", "Интерстеллар", "Титаник"]

print("Фильмы Васи:", vasyas_movies)
print("Фильмы Пети:", petas_movies)

vasyas_set = set(vasyas_movies)
petas_set = set(petas_movies)

print("Уникальные фильмы Васи:", vasyas_set)
print("Уникальные фильмы Пети:", petas_set)

only_vasya = vasyas_set.difference(petas_set)
print("Фильмы только у Васи (difference):", only_vasya)

#4
vasyas_movies = ["Матрица", "Начало", "Матрица", "Интерстеллар"]
petas_movies = ["Начало", "Аватар", "Интерстеллар", "Титаник"]

print("Фильмы Васи:", vasyas_movies)
print("Фильмы Пети:", petas_movies)

vasyas_set = set(vasyas_movies)
petas_set = set(petas_movies)

print("Уникальные фильмы Васи:", vasyas_set)
print("Уникальные фильмы Пети:", petas_set)

all_movies = vasyas_set.union(petas_set)
print("Все различные фильмы (union):", all_movies)

#5

vasyas_movies = ["Матрица", "Начало", "Матрица", "Интерстеллар"]
petas_movies = ["Начало", "Аватар", "Интерстеллар", "Титаник"]

print("Фильмы Васи:", vasyas_movies)
print("Фильмы Пети:", petas_movies)

vasyas_set = set(vasyas_movies)
petas_set = set(petas_movies)

print("Уникальные фильмы Васи:", vasyas_set)
print("Уникальные фильмы Пети:", petas_set)
ric_difference()
different_tastes = vasyas_set.symmetric_difference(petas_set)
print("Разные вкусы (symmetric_difference):", different_tastes)

#6
fruits = set()
print("Пустое множество:", fruits)

fruits.add("яблоко")
fruits.add("банан")
fruits.add("апельсин")
print("После добавления фруктов:", fruits)

fruits.remove("банан")
print("После удаления 'банана':", fruits)

fruits.discard("груша")
print("После попытки удалить 'грушу':", fruits)

has_orange = "апельсин" in fruits
print("Есть ли 'апельсин' в множестве?", has_orange)

#7
Даны два множества
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}

print("Множество A:", A)
print("Множество B:", B)

is_A_subset_of_B = A.issubset(B)
print("A является подмножеством B (issubset):", is_A_subset_of_B)

is_B_superset_of_A = B.issuperset(A)
print("B является надмножеством A (issuperset):", is_B_superset_of_A)

