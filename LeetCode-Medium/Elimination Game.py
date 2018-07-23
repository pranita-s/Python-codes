# TIME - O(logn)

def eliminationGame(n):
  
  remain = n
  step = 1
  head = 1
  left = True
  while n > 1:
    if left or remain % 2:
      head += step
    
    step *= 2
    left = not left
    remain /= 2
  
  return head
    
