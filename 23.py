import csv
with open('space.csv', newline='', encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        #print(row)
        if '0 0' in row[-2]:
            print('При получении данных о корабле', row[0], 'возникли сбои.')
            x = ''
            for i in row[3]:
                if i == ' ':
                    break
                else:
                    x += i
            #print(x)
            y = ''
            for i in reversed(row[3]):
                if i == ' ':
                    break
                else:
                    y += i
                    if y[-1] == '-':
                        y = '-'+ y[:-1]
            #print(y)
            sx = len(row[1]) - int(x)
            sy = len(row[1]) - int(y)
            print('Предположительные координаты -', sx,',', sy)
"""
spamreader - переменная, в которую вносятся 
"""