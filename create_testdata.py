import csv

data = []
num = 1
 
for i in range(1, 1000000):

    if num > 3:
        num = 1
    
    data.append(['A'+str(i).zfill(6)+','+str(num)+','+'ABCDEFGHIJKLMNOPQRST'])
    num += 1
    
    
with open('file_name', 'w') as file:
    writer = csv.writer(file, lineterminator='\n')
    for data_list in data:
        writer.writerow(data_list)
