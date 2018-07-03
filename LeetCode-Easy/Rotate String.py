# TIME - O(n)

def rotateString(A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        S = A+A
        #return S
        if len(A) != len(B):
            return False
        else:
            if B in S:
                return True
            else:
                return False
            
