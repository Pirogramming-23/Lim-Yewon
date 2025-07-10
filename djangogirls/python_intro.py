# 2 + 3; 4 * 5; 5 - 1; 40 / 2; 2 ** 3
# "Ola"
# "Hi tere " + "Ola"
# "Ola" * 3
# "Runnin' down the hill"; 'Runnin\' down the hill'
# "Ola".upper()
# len("Ola")
# len(304023) --> len(str(304023))
# name = "Ola"; name
# name = "Sonja"; name
# len(name)
# a = 4; b = 6; a * b
# city = "Tokyo"; ctiy --> NameError
# name = 'Maria'; name; print(name)
# []; lottery = [3, 42, 12, 19, 30, 59]; len(lottery); lottery.sort(); print(lottery); lottery.reverse(); print(lottery)
# lottery.append(199); print(lottery); print(lottery[0]); print(lottery[1])
# lottery.pop(0); print(lottery)
# {}; participant = {'name' : 'Ola', 'country' : 'Poland', 'favorite_numbers' : [7, 42, 92]}
# print(participant['name']); participant['age'] --> KeyError
# participant['favorite_language'] = 'Python'; len(participant)
# participant.pop('favorite_numbers'); participant
# participant['country'] = "Germany"; participant
# 5 > 2; 3 < 1; 5 > 2 * 2; 1 == 1; 5 != 2
# 6 >= 12 / 2; 3 <= 2
# 6 > 2 and 2 < 3; 3 > 2 and 2 < 1; 3 > 2 or 2 < 1
# 1 > 'django' --> TypeError
# a = True; a
# a = 2 > 5; a

print("Hello, Django girls!")

# python python_intro.py

if 3 > 2 :
    # --> SyntaxError
    print('It works!')

#python python_intro.py

if 5 > 2 :
    print('5 is indeed greater than 2')
else :
    print('5 is not greater than 2')

#python python_intro.py

name = 'Sonja'
if name == 'Ola' :
    print("Hey Ola!")
elif name == 'Sonja' :
    print('Hey Sonja!')
else :
    print('Hey anonymous!')

#python python_intro.py

volume = 57
if volume < 20 :
    print("It's kinda quiet.")
elif 20 <= volume < 40 :
    print("It's nice for background music")
elif 40 <= volume < 60 :
    print("Perfect, I can hear all the details")
elif 60 <= volume < 80 :
    print("Nice for parties")
elif 80 <= volume < 100 :
    print("A bit loud!")
else :
    print("My ears are hurting! :(")

# python python_intro.py

# voume 값을 바꿔보세요
if volume < 20 or volume > 80 :
    volume = 50
    print("That's better!")

def hi(name) :
    if name == 'Ola' :
        print("Hi Ola!")
    elif name == "Sonja" :
        print("Hi Sonja!")
    else :
        print("Hi anonymous!")

hi("Ola")
hi("Sonja")
hi("anyone")

# python python_intro.py

def hi(name) :
    print('Hi' + name + '!')

hi('Rachel')

# python python_intro.py

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for name in girls :
    hi(name)
    print('Next girl')

# python python_intro.py

for i in range(1, 6) :
    print(i)