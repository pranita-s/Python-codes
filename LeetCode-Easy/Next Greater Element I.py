 # TIME - O(m + n)
 
 def nextGreater(findNums,nums):
  s, lookup = [], {}
  
  for num in  nums:
    while s and num > s[-1]:
      lookup[s.pop()] = num    
    s.append(num)
  while s:
    lookup[s.pop()] = -1
  result = []
  for num in findNums:
    result.append(lookup[num])
  
  return result
