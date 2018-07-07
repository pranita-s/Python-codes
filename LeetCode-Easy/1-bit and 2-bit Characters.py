# TIME - O(n)

def isOneBitCharacter(bits):
  
  i = 0
  while i < len(bits)-1:
    if bits[i]:
      i += 1
    i += 1
 
  return i == len(bits)-1
