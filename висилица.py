import os
import random

clear = lambda:os.system('cls')
print("поехали")
input('нажмите enter чтобы продожить')
clear()
follower = ['беляш','самса','шаверма' ,'шурпе' ,'чиназес','хинкали','драники','чивапчичи',]
hope = random.choice(follower)
for a in hope:
    print('*',end=' ')
letters = []
is_win = True
counter = 10
while counter > 0:
    is_win = True
    letter = input('Введите букву:')
    letters.append(letter)
    for i in hope:
        if i in letters:
            print(i,end = ' ')
        else:
            print('*',end = ' ' )
            is_win = False
    print()
    if is_win:
        print('молодец,возьми с полки пирожок!')
        break
    if letter not in hope:
        counter -= 1
        print(f'ну ты и лох,но попыток осталось {counter}')
    if counter ==  0:
        print("ну ты и лох даже моя бабушка прошла,что за поколение пошло тьфу")

