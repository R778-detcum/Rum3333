#1 задание
# print("=== ШАГ 1: Создаем базовые структуры данных ===")
# mood_diary = {}
# days_of_week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
# print("Создали пустой дневник:", mood_diary)
# print("Дни недели:", days_of_week)
# print()
# print("=== ШАГ 2: Заполняем дневник настроениями ===")
# print("Введите ваше настроение для каждого дня:")
# for day in days_of_week:
#     mood = input(f"Какое у вас настроение в {day}? ")
#     mood_diary[day] = mood
# print()
# print("Дневник заполнен!")
# print()
# print("=== ШАГ 3: Ваш дневник настроений ===")
# for day, mood in mood_diary.items():
#     print(f"{day}: {mood}")
# print()
# print("=== ШАГ 4: Анализ настроений ===")
# mood_count = {}
# for mood in mood_diary.values():
#
#     if mood in mood_count:
#         mood_count[mood] += 1
#
#     else:
#         mood_count[mood] = 1
#
# print("Статистика настроений:")
# for mood, count in mood_count.items():
#     print(f"'{mood}' встречается {count} раз(а)")
#
# if mood_count:
#     most_common_mood = max(mood_count, key=mood_count.get)
#     print(f"\nСамое частое настроение: '{most_common_mood}'")
#     print(f"Оно встречалось {mood_count[most_common_mood]} раз(а)")
# else:
#     print("Дневник пустой!")
#
# print("\n=== Программа завершена ===")

#2 задание
# print("=== КУЛИНАРНАЯ КНИГА РЕЦЕПТОВ ===")
#
# recipes = {
#     "омлет": ["яйца", "молоко", "соль"],
#     "бутерброд": ["хлеб", "масло", "сыр"],
#     "салат": ["помидоры", "огурцы", "лук", "масло"]
# }
#
# print("Создали кулинарную книгу с 3 рецептами")
# print()
#
#
# def show_all_recipes():
#     print("=== ВСЕ РЕЦЕПТЫ ===")
#
#     if len(recipes) == 0:
#         print("Книга рецептов пустая!")
#         return
#
#     number = 1
#     for name, ingredients in recipes.items():
#         ingredients_text = ", ".join(ingredients)
#         print(f"{number}. {name}: {ingredients_text}")
#         number += 1
#
#
# def add_recipe():
#     print("=== ДОБАВЛЕНИЕ РЕЦЕПТА ===")
#
#     name = input("Введите название блюда: ")
#
#     print("Введите ингредиенты через запятую (например: яйца, молоко, соль): ")
#     ingredients_input = input()
#
#     ingredients_list = [ingredient.strip() for ingredient in ingredients_input.split(",")]
#
#     recipes[name] = ingredients_list
#     print(f"Рецепт '{name}' успешно добавлен!")
#
#
# def search_by_ingredient():
#     print("=== ПОИСК ПО ИНГРЕДИЕНТУ ===")
#
#     ingredient = input("Введите ингредиент для поиска: ")
#
#     found_recipes = []
#
#     for name, ingredients in recipes.items():
#         if ingredient.lower() in [i.lower() for i in ingredients]:
#             found_recipes.append(name)
#
#     if found_recipes:
#         print(f"Рецепты с ингредиентом '{ingredient}':")
#         for recipe in found_recipes:
#             print(f"- {recipe}")
#     else:
#         print(f"Рецептов с ингредиентом '{ingredient}' не найдено")
#
#
# def search_by_name():
#     print("=== ПОИСК ПО НАЗВАНИЮ ===")
#
#     name = input("Введите название рецепта: ")
#
#     found = False
#     for recipe_name, ingredients in recipes.items():
#         if name.lower() == recipe_name.lower():
#             print(f"Найден рецепт: {recipe_name}")
#             print("Ингредиенты:", ", ".join(ingredients))
#             found = True
#             break
#
#     if not found:
#         print(f"Рецепт '{name}' не найден")
#
#
# print("=== ДОБРО ПОЖАЛОВАТЬ В КУЛИНАРНУЮ КНИГУ! ===")
#
# while True:
#     print("\n" + "=" * 40)
#     print("ГЛАВНОЕ МЕНЮ:")
#     print("1 - Показать все рецепты")
#     print("2 - Добавить рецепт")
#     print("3 - Найти по ингредиенту")
#     print("4 - Найти по названию")
#     print("5 - Выйти из программы")
#     print("=" * 40)
#
#     choice = input("Выберите пункт меню (1-5): ")
#
#     if choice == "1":
#         show_all_recipes()
#     elif choice == "2":
#         add_recipe()
#     elif choice == "3":
#         search_by_ingredient()
#     elif choice == "4":
#         search_by_name()
#     elif choice == "5":
#         print("До свидания! Приятного аппетита!")
#         break
#     else:
#         print("Неверный выбор! Попробуйте снова.")
#3задание
# print("=== ЭЛЕКТРОННЫЙ ЖУРНАЛ ОЦЕНОК ===")
#
# grade_journal = {
#     "лина": [5, 4, 5, 3],
#     "руслан3": [4, 3, 4, 5],
#     "маша": [5, 5, 4, 5]
# }
#
# print("Создали журнал с 3 студентами")
# print()
#
#
# def add_student():
#     print("=== ДОБАВЛЕНИЕ НОВОГО СТУДЕНТА ===")
#
#     name = input("Введите имя студента: ")
#
#     if name in grade_journal:
#         print(f"Студент {name} уже есть в журнале!")
#         return
#
#     print("Введите начальные оценки через пробел (например: 5 4 3): ")
#     grades_input = input()
#
#     if grades_input.strip():
#         grades_list = [int(grade) for grade in grades_input.split()]
#     else:
#         grades_list = []
#
#     grade_journal[name] = grades_list
#     print(f"Студент {name} успешно добавлен!")
#
#
# def add_grade():
#     print("=== ДОБАВЛЕНИЕ ОЦЕНКИ ===")
#
#     if len(grade_journal) == 0:
#         print("В журнале нет студентов!")
#         return
#
#     print("Список студентов:")
#     students = list(grade_journal.keys())
#     for i, student in enumerate(students, 1):
#         print(f"{i}. {student}")
#
#     try:
#         choice = int(input("Выберите номер студента: ")) - 1
#         if choice < 0 or choice >= len(students):
#             print("Неверный номер!")
#             return
#
#         selected_student = students[choice]
#
#         grade = int(input(f"Введите оценку для {selected_student}: "))
#
#         if grade < 1 or grade > 5:
#             print("Оценка должна быть от 1 до 5!")
#             return
#
#         grade_journal[selected_student].append(grade)
#         print(f"Оценка {grade} добавлена студенту {selected_student}")
#
#     except ValueError:
#         print("Ошибка! Введите корректное число.")
#
#
# def calculate_average(grades):
#     if not grades:
#         return 0
#     return sum(grades) / len(grades)
#
#
# def show_all_students():
#     print("=== ВСЕ СТУДЕНТЫ ===")
#
#     if len(grade_journal) == 0:
#         print("Журнал пустой!")
#         return
#
#     print("Студент: оценки → средний балл")
#     print("-" * 40)
#
#     for student, grades in grade_journal.items():
#         avg_grade = calculate_average(grades)
#         grades_str = ", ".join(str(grade) for grade in grades) if grades else "нет оценок"
#         print(f"{student}: {grades_str} → {avg_grade:.2f}")
#
#
# def show_statistics():
#     print("=== СТАТИСТИКА ===")
#
#     if len(grade_journal) == 0:
#         print("Журнал пустой!")
#         return
#
#     students_with_avg = []
#
#     for student, grades in grade_journal.items():
#         avg_grade = calculate_average(grades)
#         students_with_avg.append((student, avg_grade, grades))
#
#     students_with_avg.sort(key=lambda x: x[1], reverse=True)
#
#     print("Студенты по успеваемости:")
#     for i, (student, avg_grade, grades) in enumerate(students_with_avg, 1):
#         print(f"{i}. {student}: {avg_grade:.2f}")
#
#     print()
#
#     best_student, best_avg, best_grades = students_with_avg[0]
#     print(f"Лучший студент: {best_student} со средним баллом {best_avg:.2f}")
#
#     worst_student, worst_avg, worst_grades = students_with_avg[-1]
#     print(f"Худший студент: {worst_student} со средним баллом {worst_avg:.2f}")
#
#     print()
#
#     excellent_students = []
#     for student, avg_grade, grades in students_with_avg:
#         if avg_grade >= 4.5 and grades:
#             excellent_students.append(student)
#
#     if excellent_students:
#         print(f"Отличники (средний балл ≥ 4.5): {', '.join(excellent_students)}")
#         print(f"Количество отличников: {len(excellent_students)}")
#     else:
#         print("Отличников нет")
#
#
# print("=== ЭЛЕКТРОННЫЙ ЖУРНАЛ ОЦЕНОК ===")
#
# while True:
#     print("\n" + "=" * 50)
#     print("ГЛАВНОЕ МЕНЮ:")
#     print("1 - Добавить студента")
#     print("2 - Добавить оценку")
#     print("3 - Показать всех студентов со средними баллами")
#     print("4 - Показать статистику")
#     print("5 - Выйти из программы")
#     print("=" * 50)
#
#     choice = input("Выберите пункт меню (1-5): ")
#
#     if choice == "1":
#         add_student()
#     elif choice == "2":
#         add_grade()
#     elif choice == "3":
#         show_all_students()
#     elif choice == "4":
#         show_statistics()
#     elif choice == "5":
#         print("До свидания! Программа завершена.")
#         break
#     else:
#         print("Неверный выбор! Попробуйте снова.")
