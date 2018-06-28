def calPoints(ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        #sum = 0
        stack = []

        for s in ops:
            if not s.isalpha() and s != '+':
                stack.append(int(s))
                #sum+=int(s)
            elif s == 'C':
                stack.pop()
            elif s == 'D':
                validPoints = 2*stack[-1]
                stack.append(validPoints)
                #sum+=validPoints
            elif s == '+':
                validPoints = stack[-1]+stack[-2]
                stack.append(validPoints)
                #sum+=validPoints
        return sum(stack)
