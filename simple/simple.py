input_data = open('simple\input.txt','r') # Создадим файл со входными данными
output = open('simple\output.txt', 'w') # Откроем файл в который будем выводить ответ
data = input_data.read ()
data = data.split()
a = int(data[0]) # Присвоим a значение из input

for i in range(2, 26): # Создадим переменную i на диапазаоне от 1 до 25
    if a%i == 0 and i !=a: # Задаим условия
        output.write(str('N')) # Вывод N
        break
    elif i == a:
        output.write(str('Y')) # Вывод Y
    if a == 1:
        output.write(str('N')) # Вывод N

input_data.close() # Закроем файл
output.close() # Закроем файл       