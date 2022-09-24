import random
tas = [1,2,3,4,5,6]
while True:
    number = random.choice(tas)
    print(number)
    if number==6:
        print('You have another chance :')
        number = random.choice(tas)
        print(number)
        break

