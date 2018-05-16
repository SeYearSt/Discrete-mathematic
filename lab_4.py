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
  
if __name__ == "__main__":
    graph = [[0, 1, 0, 1, 0],
             [1 ,0 ,1 ,1, 1],
             [0, 1, 0, 1, 0],
             [1, 1, 1, 0, 1],
             [0, 1, 0, 1, 0]]
               
    n = 4
    print("Total cycles of length ",n, " are ", countCycles(graph, n, 0))
