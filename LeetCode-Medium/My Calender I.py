
import bisect
class Calender:
  
  def __init__(self):
    self.intervals = []
  
  def book(self,start,end):
    if end <= start:
      return False
    
    s = bisect.bisect_right(self.intervals,start)
    if s % 2:
      return False
    
    e = bisect.bisect_left(self.intervals,end)
    if s != e:
      return False
    else:
      self.intervals[s:s] = [start,end]
