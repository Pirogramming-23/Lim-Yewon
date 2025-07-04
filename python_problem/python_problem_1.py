import random

num = 0
players = ["computer", "player"]
player = 0
brNum = 0

def brGame() :
    global num, player, brNum

    while True :
        try:
            num = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")
            num = int(num)
            if 1 <= num <= 3 :
                break
            else :
                print("1,2,3 중 하나를 입력하세요")
        except ValueError :
            print("정수를 입력하세요")

    for i in range(brNum, brNum+num, 1) :
        if i > 30 :
            break
        print("player:", i+1)

while True :
    if player == 0 :
        num = random.randint(1,3)
        for i in range(brNum, brNum+num, 1) :
            if i > 30 :
                break
            print("computer:", i+1)
    elif player == 1 :
        brGame()

    brNum += num
    player = (player + 1) % 2

    if brNum >= 31 :
        break

print(f"{players[player%2]} win!")