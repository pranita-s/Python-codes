# TIME - O(p + r * n), p is the count of all the possible paths in graph,
#                      r is the count of the result.
# SPACE - O(n)

def allPathsFromSourceToTarget(graph):
  
    def dfs(curr, soFar, result):
      if curr == len(graph)- 1:
        result.append(soFar[:])
      else:
        for neighbor in graph[curr]:
          soFar.append(neighbor)
          dfs(neighbor, soFar, result)
          soFar.append(neighbor)
   
   result = []
   dfs(0,[0],result)
   return result
      
