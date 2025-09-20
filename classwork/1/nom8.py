name = input ("Введите имя ")
name_len= len(name)
print(f"Длина имени : {name_len} символов")
if name_len < 3 :
    print("Имя короткое")
elif name_len==0  :
    print("Имя не введено")
else:
    print("Имя с норм длиной ")
