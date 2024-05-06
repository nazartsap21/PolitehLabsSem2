def read_input(input_file_path):
    """
    Reads the input file and creates a matrix representing of the graph

    Parameters:
        input_file_path (str): the path to the input file

    Returns:
        matrix (list[list]): the adjacency matrix of the graph.
        Returns 0 if the input_file is empty (a ValueError occurs)
    """
    matrix = []
    file = open(input_file_path, 'r')
    try:
        for line in file:
            neighbours = list(map(int, line.split(', ')))
            matrix.append(neighbours)
        file.close()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0 and i != j:
                    matrix[i][j] = float('inf')

    except ValueError:
        file.close()
        return 0

    return matrix


def write_output(output_file_path, result):
    """
    Writes the result to the output file.

    Parameters:
        output_file_path (str): the path to the output file
        result(int): the result to be written to the file
    """
    file = open(output_file_path, 'w')
    file.write(str(result))
    file.close()
    return


def floyd_warshall(matrix):
    """
    Implements the Floyd-Warshall algorithm on the given adjacency matrix.

    Parameters:
        matrix (list[list]): the adjacency matrix of the graph

    Returns:
        min_cable_length (int): the minimum cable length calculated using Floyd-Warshall algorithm
    """
    for k in range(len(matrix)):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]

    min_cable_length = 0
    for i in range(len(matrix)):
        min_cable_length += sum(matrix[i])

    return int(min_cable_length/2)


def find_minimum_cable_length(input_file_path, output_file_path):
    """
    Finds the minimum cable length required to connect all islands

    Parameters:
        input_file_path (str): the path to the input file
        output_file_path (str): the path to the output file
    """
    matrix = read_input(input_file_path)

    if matrix == 0 or matrix == -1:
        write_output(output_file_path, matrix)
    else:
        result = floyd_warshall(matrix)
        write_output(output_file_path, result)

    return
