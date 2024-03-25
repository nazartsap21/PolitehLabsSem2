import os


def get_input(file_path):
    if os.stat(file_path).st_size == 0:
        return None, None, None
    file = open(file_path, 'r')
    n = int(file.readline())
    start = tuple(map(int, file.readline().split(' ')))
    end = tuple(map(int, file.readline().split(' ')))
    file.close()
    return start, end, n


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


def shortest_chess_horse_path(start_pos, end_pos, board_s):
    if start_pos is None:
        return -1, [None]
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
        if vertex not in visited:
            if vertex == end_pos:
                return dist_to[vertex], get_path(previous_vertex, vertex, start_pos)
            visited.add(vertex)
            for direction in [(2, -1), (2, 1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]:
                row, col = vertex[0] + direction[0], vertex[1] + direction[1]
                if 0 <= row < board_s and 0 <= col < board_s and (row, col) not in visited:
                    queue.append((row, col))
                    dist_to[(row, col)] = dist_to[vertex] + 1
                    previous_vertex[(row, col)] = vertex

    return None
