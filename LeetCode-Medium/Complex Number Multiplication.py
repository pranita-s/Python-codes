# TIME - O(1)
# SPACE - O(1)

def complexNumberMultiplication(a,b):
  ra, ia = map(int, a[:-1].split('+'))
  rb, ib = map(int, b[:-1].split('+'))
  
  return '%d+%di'%(ra * rb - ia * ib, ra * ib + rb * ia)
  
  
