# TIME - O(logn)


def nextGreatestLetter(letters,target):
  
  if letters[0] > target: return letters[0]
  
  if letters[-1] <= target: return letters[0]
  
  start ,end = 0, len(letters)-1
  
  while start <= end:
    mid = (start + end)//2
    if letter[mid] > target:
      end = mid -1
    else:
      start = mid + 1
  
  return letters[start]
