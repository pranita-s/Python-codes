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
  
  
          
          
      
      
      
      
      
      
    
    
    
    
    
  
  
    
  
