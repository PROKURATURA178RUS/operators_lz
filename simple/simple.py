input_data = open('simple\input.txt','r') # Создадим файл со входными данными
data = input_data.read ()
n = int(data[0])
b = 0
output_data = open('simple\output.txt','a')
for a in range(0, 26):
    if (a%n) == 0  :
        b = ('Y')
    elif (a%n) == :
         b = ('Y')
    else:
            b = ('N')



    output_data.write(str(b) + ' ' )
input_data.close() # Закроем файл
output_data.close() # Закроем файл       