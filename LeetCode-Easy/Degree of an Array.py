# TIME - O(n)
# SPACE - O(n)

def degreeOfAnArray(nums):
  d = {}
  maxFreq = 0
  for i,num in enumerate(nums):
    if num in d:
      d[num]['count'] += 1
      d[num]['end'] = i
    else:
      d[num] = {}
      d[num]['start'] = i
      d[num]['count'] = 1
      maxFreq = max(maxFreq,d[num]['count'])
  
  minLen = 0
  for key in d:
    if d[key]['count'] == maxFreq:
      minLen = min(minLen, d[key]['end'] - d[key]['start'] + 1)
  
  return minLen
    

