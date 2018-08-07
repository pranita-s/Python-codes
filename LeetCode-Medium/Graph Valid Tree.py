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
  
  nei = collections.defaultdict(list)
  for u,v in edges:
    nei[u].append(v)
    nei[v].append(u)
  
  parent = [-1] * n
  visited = {}
  q = collections.deque([0])
  while q:
    node = q.popleft()
    visited[node] = True
    for neighbor in nei[node]:
      if parent[neighbor] != node:
        if neighbor in visited:
          return False
        else:
          parent[neighbor] = node
          visited[neighbor] = True
          q.append(neighbor)
  return True
          
          
          
          
      
      
      
      
      
      
    
    
    
    
    
  
  
    
  
