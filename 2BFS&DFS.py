from collections import deque
import time
# BFS
def bfs_route(graph, start, goal):
start_time = time.time()
queue = deque([[start]])
visited = {start}
nodes_explored = 0
while queue:
path = queue.popleft()
node = path[-1]
nodes_explored += 1
if node == goal:
return path, nodes_explored, (time.time() - start_time)
for neighbor in graph.get(node, []):
if neighbor not in visited:
visited.add(neighbor)
queue.append(path + [neighbor])
return None, nodes_explored, (time.time() - start_time)
# DFS 
def dfs_route(graph, start, goal):
start_time = time.time()
stack = [[start]]
visited = set()
nodes_explored = 0
while stack:
path = stack.pop()
node = path[-1]
if node not in visited:
visited.add(node)
nodes_explored += 1
if node == goal:
return path, nodes_explored, (time.time() - start_time)
for neighbor in reversed(graph.get(node, [])):
if neighbor not in visited:
stack.append(path + [neighbor])
return None, nodes_explored, (time.time() - start_time)
graph = {}
n = int(input("Enter number of nodes: "))
for i in range(n):
node = input(f"Enter node {i+1}: ").upper()
neighbors = input(f"Enter neighbors of {node} (space separated): ").upper().split()
graph[node] = neighbors
print("\nGraph:")
for node, neighbors in graph.items():
print(node, "->", neighbors)
start = input("\nEnter starting node: ").upper()
goal = input("Enter destination node: ").upper()
print("\nBFS:", bfs_route(graph, start, goal))
print("DFS:", dfs_route(graph, start, goal))
