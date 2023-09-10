graph = {'A':['B','C'],'B':['A','D','E'], 'D':['B','H'], 'E':['B','H'],
         'C':['A','F','G'],'F':['C','H'], 'G':['C'],'H':['D','E','F']}
print("Given Graph is:")
print(graph)


def dfs_traversal(input_graph, source):
    stack = list()
    visited_list = list()
    stack.append(source)
    visited_list.append(source)
    while stack:
        vertex = stack.pop()
        print(vertex, end=" ")
        for u in input_graph[vertex]:
            if u not in visited_list:
                stack.append(u)
            visited_list.append(u)
print("DFS traversal of graph with source A is:")
dfs_traversal(graph,"A")
