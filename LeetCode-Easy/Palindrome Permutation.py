# TIME - O(n)

# Given a string, determine if a permutation of the string could form a palindrome.


def palindromePermutation(s):
  temp = 0
  for char in s:
    val = ord(char) - ord('a')
    temp = temp ^ (1<<val)
  
  if temp == 0 or (temp & (temp-1)) == 0:
    return True
  return False
  
