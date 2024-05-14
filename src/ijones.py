def read_file(file_path):
    file = open(file_path, 'r')
    try:
        columns, lines = map(int, file.readline().split(' '))
    except ValueError:
        file.close()
        return 0

    matrix = []
    dict_of_letters = dict()
    cur_line = 0
    for line in file:
        line = line.replace('\n', '')
        cur_column = 0
        temp_line = []
        for char in line:
            temp_line.append(char)
            if char in dict_of_letters:
                dict_of_letters[char].append((cur_line, cur_column))
            else:
                dict_of_letters[char] = [(cur_line, cur_column)]

            cur_column += 1

        matrix.append(temp_line)
        cur_line += 1
    file.close()
    return matrix, dict_of_letters, lines, columns


def get_answer(matrix, dict_of_letters, lines, columns):
    letters_on_path = dict()
    letters_on_path[(0, columns - 1)] = []
    letters_on_path[(lines - 1, columns - 1)] = []
    for column in range(columns - 2, -1, -1):
        for row in range(0, lines):
            was_in_neighbour = False
            for neighbour in dict_of_letters[matrix[row][column]]:
                if neighbour in letters_on_path and neighbour[1] > column:
                    letters_on_path[neighbour].append((row, column))
                    letters_on_path[(row, column)] = []
                if neighbour == (row, column + 1):
                    was_in_neighbour = True

            if was_in_neighbour or (row, column + 1) not in letters_on_path:
                continue
            letters_on_path[(row, column + 1)].append((row, column))
            letters_on_path[(row, column)] = []
    return letters_on_path


def get_paths(dict_of_paths, lines, columns):
    stack = [(0, columns - 1)]
    if lines - 1 != 0:
        stack.append((lines - 1, columns - 1))

    result = 0
    while stack:
        current_row, current_column = stack.pop()
        if current_column == 0:
            result += 1
            continue
        for neighbour in dict_of_paths[(current_row, current_column)]:
            stack.append(neighbour)

    return result


def write_result(output_file, result):
    file = open(output_file, 'w')
    file.write(str(result))
    file.close()


def ijones(input_file, output_file):
    ijones_matrix, letters_dict, lines, cols = read_file(input_file)
    dict_ijones = get_answer(ijones_matrix, letters_dict, lines, cols)
    result = get_paths(dict_ijones, lines, cols)
    write_result(output_file, result)
