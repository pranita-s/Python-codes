# TIME - O(n)
# SPACE - O(n)

def palindromicSubstrings(s):
  
  def manachers(s):
    T = '^#' + '#'.join(s) + '#$'
    P = [0] * len(T)
    C, R = 0, 0
    for i in range(1,len(T)-1):
      mirror = 2 * C - i
      
      if R > i:
        P[i] = min(R - i, P[mirror])
       
      while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
        P[i] += 1
      
      if i + P[i] > R:
        C = i
        R = i + P[i]
    
    return sum((summ+1)/2 for summ in P)
  
  return manachers(s)
