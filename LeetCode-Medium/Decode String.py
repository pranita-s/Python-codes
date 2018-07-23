# TIME - O(n)
# SPACE - O(n)


def decodeString(s):
  # "3[a2[c]]"
  stk = [["",1]]
  num = ""
  for char in s:
    if char.isdigit():
      num += char
    elif char == '[':
      stk.append(["",int(num)])
      num = ""
    elif char == ']':
      string,count = stk.pop()
      stk[-1][0] += string * count     
    else:
      stk[-1][0] += char
   
   return stk[0][0]
      
  
