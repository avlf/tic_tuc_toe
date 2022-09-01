from bot_logic import Bot
from map import Map


def start():
    width = int(input('type width '))
    height = int(input('type height '))
    n = int(input('type num of bots'))
    win_condition=int(input('type win condition'))
    map = Map(width, height)
    map.drow_map()
    game = True
    wc = min(width, height)
    mass=[]*n
    for i in range(n):
        mass[i] = Bot(i, wc,win_condition=3)
    while game:
        for  i in range(n):
            game = mass[i].turn(map)
            map.drow_map()
            print()
            if not game:
                print(i)
                break
            game = mass[i].turn(map)
            map.drow_map()
            print()
                # d/z 1 реализовать создание произвольнго количества ботов с клавиатуры
                # для каждого бота символ
                # win_condition с клавиатуры
                # КАК ЗАКОНЧИЛАСЬ ИГРА ПОЧИТАТЬ ПРО GIT(КОМАНДЫ)


start()
