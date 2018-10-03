# BFS -> O(V+E) (adjacency list)
# Union Find -> O(ElogV)

def graphValidTree(n,edges):
  if len(edges) != (n-1):
    return False
  
  visited = {}
  neighbors = collctions.defaultdict(list)
  for u,v in edges:
    neighbors[u].append(v)
    neighbors[v].append(u)
  
  q = collections.deque([0])
  while q:
    node = q.popleft()
    visited[node] = True
    for n in neighbors[node]:
      if n not in visited:
        q.append(n)
    visited.append(node)
  
  return len(visited) == n


def graphValidTree2(n,edges):
  if len(edges) != n-1:
    return False
  
  graph = collections.defaultdict(list)
  
  for u,v in edges:
    graph[u].append(v)
    graph[v].append(u)
  
  visited = [False] * n
  parent = [-1] * n
  q = collections.deque([0])
  while q:
    node = q.popleft()
    visited[node] = True
    for neighbor in graph[node]:
      if neighbor != parent[node]:
        if visited[neighbor]:
          return False
        else:
          parent[neighbor] = node
          a.append(neighbor)
          visited[neighbor] = True
   return True
  
  
          
          
 
def graphValidTree():
  
  def hasCycle(cur,parent):
    
    visited[cur]= True
    for nei in g[cur]:
      if visited.get(nei,False) == False:
        if hasCycle(nei,cur) == True:
          return True
         # If an adjacent is visited and not  
            # parent of current vertex, then there  
            # is a cycle.
      elif nei != parent:
        return True
    return False
  
  visited = {}
  if hasCycle(0,-1): 
    return False
  
  return len(visited)==num_vertices
  
      
      
     
    
    
    
  
  
    
  
