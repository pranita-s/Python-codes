
# TIME - O(1)

def constructRectangle(area):
  import math
  mid = int(math.sqrt(area))
  
  while area % mid != 0:
    mid -= 1
  
  return (area//mid,mid)
