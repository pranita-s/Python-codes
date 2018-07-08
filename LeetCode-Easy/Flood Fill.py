
# TIME - O(R * C)


def floodFill(grid,i,j,newColor,oldColor)
  
  def floodFillHelper(grid,i,j,newColor,oldColor):    
    if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == oldColor:
      grid[i][j] = newColor
      floodFillHelper(grid,i-1,j,newColor,oldColor)
      floodFillHelper(grid,i+1,j,newColor,oldColor)
      floodFillHelper(grid,i,j-1,newColor,oldColor)
      floodFillHelper(grid,i,j+1,newColor,oldColor)
   return grid
  
   return floodFillHelper(grid,i,j,newColor,oldColor) if grid[i][j] != newColor else grid
   
   

      
      
  
  
  
