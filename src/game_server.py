from src.avl_priority_queue import *


def write_output(output_file_path, result):
    file = open(output_file_path, 'w')
    file.write(str(result))
    file.close()
    return


def dijkstra(server, vertex_n, gamers, adjacency_list):
    temp_max_ping = 0
    priority_queue = AVLTree()
    priority_queue.enqueue(server, 0)
    dist_to = {}
    for vertex in range(vertex_n + 1):
        dist_to[vertex] = float('inf')
    dist_to[server] = 0
    visited = set()
    while priority_queue:
        node = priority_queue.deque()
        if node is None:
            break
        vertex = node[0]
        if vertex in gamers:
            temp_max_ping = max(temp_max_ping, dist_to[vertex])
        if vertex in visited:
            continue
        visited.add(vertex)
        for neighbour, weight in adjacency_list[vertex - 1]:
            if dist_to.get(neighbour, float('inf')) > dist_to[vertex] + weight:
                dist_to[neighbour] = dist_to[vertex] + weight
                priority_queue.enqueue(neighbour, dist_to[neighbour])
    return temp_max_ping


def game_ping(input_file_path, output_file_path):
    file = open(input_file_path, 'r')
    try:
        vertex_n, edge_n = tuple(map(int, file.readline().split(' ')))
        gamers = list(map(int, file.readline().split(' ')))
        router_list = [router for router in range(1, vertex_n + 1) if router not in gamers]
        adjacency_list = [[] for _ in range(vertex_n)]
        for i in (range(edge_n)):
            vertex, neighbour, weight = tuple(map(int, file.readline().split(' ')))
            adjacency_list[vertex - 1].append((neighbour, weight))
            adjacency_list[neighbour - 1].append((vertex, weight))
        file.close()
    except ValueError:
        write_output(output_file_path, -1)
        file.close()
        return

    min_ping = float('inf')
    for server in router_list:
        min_ping = min(min_ping, dijkstra(server, vertex_n, gamers, adjacency_list))

    with open(output_file_path, 'w') as file:
        file.write(str(min_ping))
    return None
