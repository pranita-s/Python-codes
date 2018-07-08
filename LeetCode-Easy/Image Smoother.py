# TIME - O(R * C)
# SPACE - O(R * C)

def imageSmoother(grid):
  
  smooth = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
  
  def helper(grid, i, j):
    count = 0
    addition = 0
    neighbors = [[i-1,j-1],[i-1,j],[i-1,j+1],[i,j+1],[i+1,j+1],[i+1,j],[i+1,j-1],[i,j-1]]
            for n in neighbors:
                if 0<= n[0] < len(M) and 0<= n[1] < len(M[0]):
                    addition += M[n[0]][n[1]]
                    count+=1
            smooth[i][j] = (addition//count)
    
    
    
  
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      helper(grid,i,j)
  
  return smooth
  
