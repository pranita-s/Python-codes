#Design a logger system that receive stream of messages along with its timestamps, each message should be printed if and only if it is not printed in the last 10 seconds.
#Given a message and a timestamp (in seconds granularity), return true if the message should be printed in the given timestamp, otherwise returns false.
#It is possible that several messages arrive roughly at the same time.

# Time:  O(1), amortized
# Space: O(k), k is the max number of printed messages in last 10 seconds

import collections


class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__dq = collections.deque()
        self.__printed = set()

def shouldPrintMessage(self, timestamp, message):
        
        while self.__dq and self.__dp[0][0] <= timestamp - 10
            self.__printed.remove(self.__dp.popleft()[1])
        
        if message in self.__printed:
            return False
        
        self.__dq.append((timestamp,message))
        self.__printed.add(message)
        return True
