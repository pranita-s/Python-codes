# TIME - O(n)
# SPACE - O(num_chars)

def customSortString(S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        
        lookup = {c:0 for c in S}
        notS = {}
        for c in T:
            if c in lookup:
                lookup[c]+=1
            else:
                notS[c] = 1 + notS.get(c,0)
        res=''
        for c in S:
            if lookup[c]!=0:
                while lookup[c]:
                    res+=c
                    lookup[c]-=1
        for c in notS:
            while notS[c]:
                res+=c
                notS[c]-=1
        return res
        
