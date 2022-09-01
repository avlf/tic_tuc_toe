def check_win(map, x, y):
    right = [1, 0]
    left = [-1, 0]
    up = [0, -1]
    down = [0, 1]
    ld_up = [-1, -1]
    ld_down = [-1, 1]
    rd_up = [1, -1]
    rd_down = [1, 1]
    lr = check_direction(map, x, y, right) + check_direction(map, x, y, left) - 1
    ud = check_direction(map, x, y, up) + check_direction(map, x, y, down) - 1
    ld = check_direction(map, x, y, ld_up) + check_direction(map, x, y, rd_down) - 1
    rd = check_direction(map, x, y, rd_up) + check_direction(map, x, y, ld_down) - 1

    if max(lr, ud, ld, rd) >= 3:
        return True
    return False


def check_direction(map, cur_x, cur_y, change):
    count = 0
    while cur_x >= 0 and cur_x <= len(map[1]) - 1 and cur_y >= 0 and cur_y <= len(map) - 1 and map[cur_x][cur_y] == 'x':
        count += 1
        cur_y += change[1]
        cur_x += change[0]
    return count


mymap = [
    ['x', 'o', 'x'],
    ['x', 'x', 'o'],
    ['x', 'o', '0']
]
print(check_win(mymap,0,0))