# TIME - ?? 

def keysAndRooms(rooms):
  
  visited = [False] * len(rooms)
  def dfs(curr):
    if visited[curr] == False:
      for neighbor in rooms[curr]:
        dfs(neighbor)
  
  dfs(0)
  if all(v==True for v in visited):
    return True
  else:
    return False
