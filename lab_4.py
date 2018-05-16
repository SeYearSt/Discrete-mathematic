import networkx as nx
import matplotlib.pyplot as plt

V = 5
 
def DFS(graph, marked, n, vert, start, count):
    
    marked[vert] = True

    if n == 0:
        
        marked[vert] = False
        
        if graph[vert][start] == 1:
            count = count + 1
            return count
        else:
            return count
        
    for i in range(V):
        if marked[i] == False and graph[vert][i] == 1:
            
            count = DFS(graph, marked, n-1, i, start, count)
  
    marked[vert] = False
    return count
  
def countCycles(graph, n, vert):
    
    marked = [False] * V 
  
    count = 0
   
    count = DFS(graph, marked, n-1, vert, vert, count)
        
    return count

def draw_graph():
    plt.figure(figsize=(12, 4))
    plt.axis('off')

    nx.draw_networkx_nodes(graph, layout, node_color='steelblue', node_size=600)
    nx.draw_networkx_edges(graph, layout, edge_color='gray')
    nx.draw_networkx_labels(graph, layout, font_color='white')

    for u, v, e in graph.edges(data=True):
        color = 'green'
        #if e['flow'] < e['capacity'] else 'red'
        x = layout[u][0] * .6 + layout[v][0] * .4
        y = layout[u][1] * .6 + layout[v][1] * .4
            
    plt.show()

  
if __name__ == "__main__":
    graph = [[0, 1, 0, 1, 0],
             [1 ,0 ,1 ,1, 1],
             [0, 1, 0, 1, 0],
             [1, 1, 1, 0, 1],
             [0, 1, 0, 1, 0]]
    n = 3

    print("Total cycles of length ",n - 1, " are ", countCycles(graph, n, 0))

    
    graph = nx.DiGraph()
    graph.add_nodes_from('ABCDE')
    graph.add_edges_from([
        ('A', 'B'),
        ('B', 'A'),
        ('B', 'C'),
        ('B', 'D'),
        ('B', 'E'),
        ('C', 'B'),
        ('C', 'D'),
        ('D', 'A'),
        ('D', 'B'),
        ('D', 'C'),
        ('D', 'E'),
        ('E', 'B'),
        ('E', 'D')
    ])

    layout = {
    'A': [0, 0], 'B': [0, 2], 'C': [1, 3], 'D': [2, 2],
    'E': [1, 0]}

    draw_graph()
    
    input('End')
