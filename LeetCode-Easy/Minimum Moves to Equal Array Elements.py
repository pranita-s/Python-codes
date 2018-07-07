# TIME - O(n)


def moves(nums):
  minNum = sys.maxint
  moves = 0
  for num in nums:
    minNum = min(num,minNum)
  
  for num in nums:
    moves += (num - minNum)
  
  return moves
  
