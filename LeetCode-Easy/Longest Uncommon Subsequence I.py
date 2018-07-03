# TIME - O(min(m,n))


def LongestUncommonSequence(s1,s2):
  if s1 ==s2:
    return -1
  return max(len(s1),len(s2))
