import random


class Bot:
    def __init__(self, symbol, win_condition=3):
        self.symbol = symbol
        self.win_condition = win_condition
        self.name = ' '.join([self.symbol, 'bot'])

    def gen_dot(self, playground):
        dot_x = random.randint(0, playground.width - 1)
        dot_y = random.randint(0, playground.height - 1)
        while playground.field[dot_y][dot_x] != 0:
            dot_x = random.randint(0, playground.width - 1)
            dot_y = random.randint(0, playground.height - 1)
        return (dot_y, dot_x)

    def turn(self, playground):
        dot = self.gen_dot(playground)
        playground.field[dot[0]][dot[1]] = self.symbol
        game_continues = self.chek_game_continues(playground, dot)
        return game_continues

    def chek_game_continues(self, playground, dot):
        '''
        ВОЗВРАЩАЕТ  труе если продолжаем false если заканчиваем
        '''
        resultFinal = True
        result_drow = self.check_drow(playground)
        result_win = self.check_win(playground, dot[0], dot[1])
        if result_drow == True or result_win == True:
            resultFinal = False
        return resultFinal

    def check_drow(self, playground):
        '''
        проверем заполнение поля
        :return:
        '''
        result = True
        for i in range(playground.height):
            for j in range(playground.width):
                if playground.field[i][j] == 0:
                    result = False
                    return result
        return result

    def check_win(self, playground, x, y):
        right = [1, 0]
        left = [-1, 0]
        up = [0, -1]
        down = [0, 1]
        ld_up = [-1, -1]
        ld_down = [-1, 1]
        rd_up = [1, -1]
        rd_down = [1, 1]
        lr = self.check_direction(playground, x, y, right) + self.check_direction(playground, x, y, left) - 1
        ud = self.check_direction(playground, x, y, up) + self.check_direction(playground, x, y, down) - 1
        ld = self.check_direction(playground, x, y, ld_up) + self.check_direction(playground, x, y, rd_down) - 1
        rd = self.check_direction(playground, x, y, rd_up) + self.check_direction(playground, x, y, ld_down) - 1

        if max(lr, ud, ld, rd) >= self.win_condition:
            return True
        return False

    def check_direction(self, playground, cur_x, cur_y, change):
        count = 0
        while cur_x >= 0 and cur_x <= len(playground.field[1]) - 1 and cur_y >= 0 and cur_y <= len(playground.field) - 1 and \
                playground.field[cur_x][cur_y] == self.symbol:
            count += 1
            cur_y += change[1]
            cur_x += change[0]
        return count
