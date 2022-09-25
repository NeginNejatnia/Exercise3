test = input('enter time: ')
print(test)
temp = test.split(':')
h = (int(temp[0]))*3600
d = (int(temp[1]))*60
s = int(temp[2])
second = h+d+s
print('second : ',second)


