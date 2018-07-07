# TIME - O(n)

def largeGroupPositions(S):
    
    i = 0
    pos = []
    for j in range(1,len(S)):
      if j > 0 and S[j] != S[j+1]:
        if j-1+1 >= 3:
          pos.append([i,j])
        i = j + 1
    return pos
