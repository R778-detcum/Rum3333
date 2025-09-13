from idlelib.pyshell import fix_x11_paste

num1 = float (input("Введите первое число:"))
num2 = float (input("Введите второе число:"))
num3 = float (input("Введите третье число:"))
cool=max(num1, num2, num3)
print(f"Наибольшее число среди {num1}, {num2}, {num3} : {cool}")