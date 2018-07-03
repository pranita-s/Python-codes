# TIME - O(n)

def detectCapital(word):
  
  if all(w.islower for w in word) or all(w.isupper() for w in word):
    return True
  elif word[0].isupper() and all(w.islower() for w in word[1:]):
    return True
  else:
    return False
