# Time:  O(nlogn)
# Space: O(n)


# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] 
#(si < ei), determine if a person could attend all meetings.
#For example, Given [[0, 30],[5, 10],[15, 20]], return false. 

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

def meetingRooms(meetings):

  meetings.sort(key = lambda x : x.start)
  
  for i in xrange(1, len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                return False
  return True
  
  
