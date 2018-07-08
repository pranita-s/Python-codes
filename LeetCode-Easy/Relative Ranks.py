# TIME - O(n)
# SPACE - O(n)

def relativeRanks(nums):
  
  d = {num:i for i,num in enumerate(sorted(nums,reverse = True))}
  res = []
  medals = ['Gold Medal','Silver Medal','Bronze Medal']
  
  for num in nums:
    if d[num] < len(medals):
      res.append(medals[d[num]])
    else:
      res.append(str(d[num]+1))
  
  return res
  
