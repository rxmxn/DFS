import sys
import threading

threading.stack_size(67108864)
sys.setrecursionlimit(10 ** 6)


def get_input(filename):
    graph_map = {}

    for line in open(filename, 'r').readlines():
        values = [int(val) for val in line.split()]
        key1 = values.pop(0)
        key2 = values.pop(0)

        if not key1 in graph_map:
            graph_map[key1] = []

        if not key2 in graph_map:
            graph_map[key2] = []

        graph_map[key1].extend([key2])

    return graph_map


def DFS(graph_map, start):
    global visited

    visited[start-1] = True

    for child in graph_map[start]:
        if visited[child-1] is False:
            DFS(graph_map, child)


def DFS_Loop(graph_map):
    global visited

    i = len(graph_map)  # max(graph_map.keys())
    for i in reversed(range(1, i+1)):
        if visited[i-1] is False:
            DFS(graph_map, i)


graph_map = get_input("SCC.txt")
#print(graph_map)
visited = [False]*len(graph_map)  # size of the graph
DFS_Loop(graph_map)