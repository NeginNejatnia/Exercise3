from audioop import avg
import statistics

tedad = int(input('Enter number of students : '))
list = []
for i in range(tedad):
    nomarat = float(input('Enter mark of studens : '))
    list.append(nomarat)
avg=statistics.mean(list)
    
print('avg',avg)
print('max',max(list))
print('min',min(list))

