# TIME - O(n)

def keyboardRow(words):
  a = set('qwertyuiop')
  b = set('asdfghjkl')
  c = set('zxcvbnm')
  result = []
  for word in words:
    w = set(word.lower())
    if (w&a == w | w&b == w | w&c == w):
      result.append(word)
  return result
