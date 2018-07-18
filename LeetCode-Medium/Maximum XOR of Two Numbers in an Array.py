# TIME - O(n)


def findMaxXOR(nums):
  root = {}
  maxXor = -float('inf')
  tree = bit
  for num in nums:
    binary = format(num,'b').zfill(32)
    for bit in binary:
      if tree.get(bit):
        tree[bit] = {}
      tree = tree[bit]
    tree['value'] = num
    tree = root
    
    for bit in binary:
      if bit == '0' and tree.get('1'):
        tree = tree['1']
      elif bit == '1' and tree.get('0'):
        tree = tree['0']
      else:
        tree = tree[bit]
      
     maxXor = max(maxXor, tree['value'] ^ num)
     tree = root
   
   return maxXor
