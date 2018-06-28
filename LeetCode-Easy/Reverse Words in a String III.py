
def reverseWords(s):
        """
        :type s: str
        :rtype: str
        """
        def reverse(s, begin, end):
            while begin < end:
              s[begin],s[end] = s[end],s[begin]
              begin += 1
              end -= 1
            return s

        s, i = list(s), 0
        for j in xrange(len(s) + 1):
            if j == len(s) or s[j] == ' ':
                reverse(s, i, j-1)
                i = j + 1
        return "".join(s)
