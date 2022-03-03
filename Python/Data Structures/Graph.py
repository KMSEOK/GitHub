# 그래프 정점집합 v와 간선 edge집합 e 
# G = (v,e)
# 차수Degree, 진입/진출 = in/out-Dergee, 경로path: 임의의 시작점에서 임의의 도착점 까지의 정점들의 나열
# 단순경로 simple Path = path의 경로중 동일노드 복수 출현 불허
# 싸이클 cycle = 시작점과 도착점이 동일한 단순 경로
# 연결 성분 connected component = 정점들이 서로 연결되어있는 부분
# 가중치 weighted graph : 간선 간의 가중치가 부여된 그래프
# 부분 그래프 Subgraph = 주어진 그래프의 부분 집합
# 트리 tree = 사이클이없고 하나의 연결 성분으로 구성된 그래프
# 신장 트리 Spanning tree = 그래프의 모든 정점들을 싸이클 없이 연결하는 부분 그래프

class Node:

    def __init__(self, data):
        self.data = data
        self.neighbors = []
        self.visited = False
    
    def add_neighbor(self, node):
        self.neighbors.append(node)

    def set_visited(self, visited):
        self.visited = visited

    def get_data(self):
        return self.data
    
    def get_neighbors(self):
        return self.neighbors
    
    def get_visited(self):
        return self.visited

class Graph:

    def __init__(self):
        self.nodes = []
    
    def add_node(self, node):
        self.nodes.append(node)

    def print_node(self):
        for node in self.nodes:
            print(node.get_data())

    def bfs(self):
        pass



graph = Graph()

node_A = Node("A")
graph.add_node(node_A)
node_B = Node('B')
graph.add_node(node_B)
node_C = Node('C')
graph.add_node(node_C)
node_D = Node('D')
graph.add_node(node_D)
node_E = Node('E')
graph.add_node(node_E)
node_F = Node('F')
graph.add_node(node_F)
node_G = Node('G')
graph.add_node(node_G)
node_H = Node('H')
graph.add_node(node_H)
node_S = Node('S')
graph.add_node(node_S)

graph.print_node()

node_A.add_neighbor(node_B)
node_A.add_neighbor(node_S)

node_B.add_neighbor(node_A)

node_S.add_neighbor(node_A)
node_S.add_neighbor(node_C)
node_S.add_neighbor(node_G)

node_C.add_neighbor(node_D)
node_C.add_neighbor(node_E)
node_C.add_neighbor(node_F)
node_C.add_neighbor(node_S)

node_D.add_neighbor(node_C)

node_F.add_neighbor(node_C)
node_F.add_neighbor(node_G)

node_G.add_neighbor(node_F)
node_G.add_neighbor(node_S)
node_G.add_neighbor(node_H)

node_E.add_neighbor(node_H)
node_E.add_neighbor(node_C)

print("BFS result")
graph.bfs()