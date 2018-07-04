# TIME - O(m + n)
# SPACE - O(m + n)

def backspaceCompare(S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s1,s2 = [], []
        
        for char in S:
            if s1 and char == '#':
                s1.pop()
            elif char != '#':
                s1.append(char)
        
        for char in T:
            if s2 and char == '#':
                s2.pop()
            elif char != '#':
                s2.append(char)
        print(s1,s2)
        if not s1 and not s2:
            return True
        else:
            return s1==s2
