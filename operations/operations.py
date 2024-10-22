input_data = open('operations\input.txt','r') # Создадим файл со входными данными
data = input_data.read ()
data = data.split()
a = int(data[0]) # Присвоим a значение из input
b = 0
while a != 0: # Условия
    if a%3 == 0:
        a -= 3
    elif a%3 == 1:
        a -= 1
    elif a%3 == 2:
        a -= 2
    b += 1
output = open('operations\output.txt', 'w') # Откроем файл в который будем выводить ответ
output.write(str(b)) # Выведем ответ
input_data.close() # Закроем файл
output.close() # Закроем файл       