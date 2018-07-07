# TIME - O(m + n)
# SPACE - O(m + n)

import collections
def mostCommonWord(paragraph, banned):
  
  lookup = set(banned)
  words = collections.Counter(word.strip("!?';.") for word in paragraph.lower().split())
  result = ''
        for word in counts:
            if (not result or counts[word] > counts[result]) and \
               word not in lookup:
                result = word
  return result
