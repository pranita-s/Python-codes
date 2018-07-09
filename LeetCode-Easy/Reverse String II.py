# TIME -O(n)
# SPACE - O(1)


def reverseStringII(s,k):
  answer = ''
  start, end = 0, 2*k
  while s:
    temp1= s[:2k]
    temp2 = s[:k]
    temp2 = temp[::-1]
    answer += temp2 + temp1[k:]
    s= s[2k:]
  
  return answer
  

def reverseStringII(s)
  s = list(s)
  for i in range(0,len(s),2*k):
    s[i:i+k] = s[i:i+k:-1]
  return ''.join(s)
