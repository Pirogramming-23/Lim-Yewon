num = 0
brNum = 0

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
    print("playerA:", i+1)
brNum += num

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
    print("playerB:", i+1)
brNum += num