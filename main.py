import random 
computer = random.randint(0,10)
while True:
    print('guessing number')
    player = int(input('guess the number'))
    if player > 10:
        print ('number cant be greater than 10')
        break
    if player == computer:
        print('you guessed right')
        break
    else:
        print('you guessed wrong')
        get_hint = input("get hint? (y/n): ")
        if get_hint.lower() != "y":
            break
    if computer % 2:
        print('number is odd')
    else:
        print('number is even')
    if computer<=5:
        print ('number is in between 1 to 5 ')
    elif computer >=5 and  player <= 10:
        print('number is between 5-10')
    else:
        print(computer)
    break