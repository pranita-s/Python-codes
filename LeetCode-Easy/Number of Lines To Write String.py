# TIME - O(len_S)


def numberOfLines(widths,S):
  curr = 0
  lines = 1
  for c in S:
    w = widths[ord(c)-ord('a')]
    if curr + w > 100:
      curr = w
      lines += 1
    else:
      curr += w
  return [lines,curr]
