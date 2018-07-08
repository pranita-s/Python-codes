# TIME - O(n)

def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        countA,count2L=0,0

        for i in range(len(s)):
            if s[i] == 'A': countA+=1
            if countA > 1:
                return False
            if s[i] == 'L' and i < len(s)-2:
                if s[i+1]=='L' and s[i+2]=='L':
                    return False

        return True
