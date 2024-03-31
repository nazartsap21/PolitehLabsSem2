def write_output(file_path, answer):
    file = open(file_path, 'w')
    file.write(str(answer[0]) + '\n')
    file.write(str(answer[1]))
    file.close()


def get_path(from_dict, last_vertex, start_vertex):
    path = []
    while last_vertex != start_vertex:
        path.append(last_vertex)
        last_vertex = from_dict[last_vertex]
    path.append(start_vertex)
    return path[::-1]


def find_shortest_chess_horse_path(input_file_path, output_file_path):
    file = open(input_file_path, 'r')
    try:
        board_s = int(file.readline())
        start_pos = tuple(map(int, file.readline().split(' ')))
        end_pos = tuple(map(int, file.readline().split(' ')))
    except ValueError:
        write_output(output_file_path, (-1, [None]))
        file.close()
        return
    file.close()

    queue = [start_pos]
    dist_to = {
        start_pos: 0,
    }
    previous_vertex = {
        start_pos: None,
    }
    visited = set()

    while queue:
        vertex = queue.pop(0)
        if vertex in visited:
            continue

        if vertex == end_pos:
            write_output(output_file_path, (dist_to[vertex], get_path(previous_vertex, vertex, start_pos)))
            break
        visited.add(vertex)
        for direction in [(2, -1), (2, 1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]:
            row, col = vertex[0] + direction[0], vertex[1] + direction[1]
            if 0 <= row < board_s and 0 <= col < board_s and (row, col) not in visited:
                queue.append((row, col))
                dist_to[(row, col)] = dist_to[vertex] + 1
                previous_vertex[(row, col)] = vertex
    return None
