# TIME - O(n * 2 ** n)
# SPACE - O(n * 2 ** n)


def letterCasePermutation(S):
  
  def changeCase(ch):
    return ch.upper() if ch.lower else ch.lower()
  
  def becktrack(res,S,start):
    res.append(S)
    for i in range(start,len(S)):
      if not S[i].isalpha():
        continue
      S = S[:i] + changeCase(S[i]) + S[i+1:]
      backtrack(res,S,i+1)
      S = S[:i] + changeCase(S[i]) + S[i:]
  
  res =[]
  backtrack(res,S,0)
  return res
