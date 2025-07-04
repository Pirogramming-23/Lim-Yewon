num = 0
players = ["playerA", "playerB"]
turn = 0
brNum = 0

while True :
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
        print(f"{players[turn%2]}:", i+1)
    brNum += num
    turn += 1

    if brNum >= 31 :
        break

print(f"{players[turn%2]} win!")