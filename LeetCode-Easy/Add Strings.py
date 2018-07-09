# TIME - O(max(M,N))


def addStrings(num1, num2):
  result = []
  i,j = len(num1)-1, len(num2)-1
  carry = 0
  while i >= 0 or j >= 0 or carry:
    if i >= 0:
      carry += ord(nums1[i]) - ord('0')
      i -= 1
   if j >= 0:
      carry += ord(num2[j]) - ord('0')
      j-=1
    result.insert(0,str(carry%10))
      carry = carry/10
        
  return ''.join(result)
      
  
