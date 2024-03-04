def zigzag(n: int, m: int) -> list:

    def down_left_move():
        nonlocal line, column, number
        while line < n and column >= 0:
            td_array[line][column] = number
            number += 1
            line += 1
            column -= 1
        line -= 1
        column += 1

    def up_right_move():
        nonlocal line, column, number
        while line >= 0 and column < m:
            td_array[line][column] = number
            number += 1
            line -= 1
            column += 1
        line += 1
        column -= 1

    td_array = [[0] * m for _ in range(n)]
    result = []
    line, column = 0, 0
    number = 1
    while line < n and column < m:
        if line == 0 and column == 0:
            td_array[line][column] = number
            number += 1

        if column + 1 < m:
            column += 1
            down_left_move()
        elif line + 1 < n:
            line += 1
            down_left_move()

        if line + 1 < n:
            line += 1
            up_right_move()
        elif column + 1 < m:
            column += 1
            up_right_move()

        if line == n - 1 and column == m - 1:
            break

    for i in range(n):
        result.extend(td_array[i])

    return result
