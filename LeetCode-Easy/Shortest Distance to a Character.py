# TIME - O(n)

def shortestToChar(S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        result = [float('inf')] * len(S)
        prev = -float('inf')
        
        for i,c in enumerate(S):
            if c == C:
                result[i] = 0
                prev = i
            else:
                result[i] = min(result[i],abs(i-prev))
        
        for i,c in enumerate(reversed(S)):
            i = len(S)-1-i
            if c == C:
                result[i] = 0
                prev = i
            else:
                result[i] = min(result[i],abs(i-prev))
    
        return result
