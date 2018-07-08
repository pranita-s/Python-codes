# TIME - O(n)

def ransomNote(ransomNote, magazine):
  
  return all(ransomNote.count(i) <= magazine.count(i) for i in ransomNote)
