from src.avl_priority_queue import *


def write_output(output_file_path, result):
    file = open(output_file_path, 'w')
    file.write(str(result))
    file.close()
    return


def create_adjacency_list(matrix):
    adjacency_list = [[] for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:
                adjacency_list[i].append((j, matrix[i][j]))

    return adjacency_list


def prims_algorithm(adj_list):
    visited = set()
    priority_queue = AVLTree()
    max_cable_length = 0
    priority_queue.enqueue(0, 0)

    while len(visited) < len(adj_list):
        current_island = priority_queue.deque()
        max_cable_length += current_island[1]
        neighbours = adj_list[current_island[0]]

        for neighbour in neighbours:
            if neighbour[0] not in visited:
                priority_queue.enqueue(neighbour[0], neighbour[1])
        visited.add(current_island[0])

    return max_cable_length


def find_minimum_cable_length(input_file, output_file):
    matrix = []
    file = open(input_file, 'r')
    try:
        for line in file:
            neighbours = list(map(int, line.split(', ')))
            matrix.append(neighbours)
        file.close()
    except ValueError:
        write_output(output_file, 0)
        file.close()
        return

    adjacency_list = create_adjacency_list(matrix)
    if [] in adjacency_list:
        write_output(output_file, -1)
    else:
        result = prims_algorithm(adjacency_list)
        write_output(output_file, result)
