input_data = open('input.txt','r') # Создадим файл со входными данными
data = input_data.read ()
data = data.split()
b = int(data[0]) # Каждой переменной присвоим значение из файла со входными данными
q = int(data[1])
n = int(data[2])
output_data = open('output.txt','a') # Создадим файл с выходными данными
for a in range(1, 1000):                 # Создадим цикл for и в нем переменную a 
    if((b *(1-(q**n)))/(1 - q)) == a:    # Запишем формулу геометрической прогресии
        output_data.write(str(a) + '')   # Выведем ответ

input_data.close() # Закроем файл
output_data.close() # Закроем файл   