# TIME - O(n)

def scoreOfParenthesis(s):
  depth, score = 0, 0
  for i, char in enumerate(s):
    if char == '(':
      depth += 1
    else:
      depth -= 1
      if s[i-1] == '(':
        score += 2 ** depth
  return score
