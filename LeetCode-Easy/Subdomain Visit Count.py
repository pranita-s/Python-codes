
def subdomainVisits(cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        result = []
        d = {}
        delimiters = " ","."
        regexPattern = '|'.join(map(re.escape, delimiters))
        for domain in cpdomains:
            dot_splitted = re.split(regexPattern,domain)
            d['.'.join(dot_splitted[1:])] = d.get('.'.join(dot_splitted[1:]),0) + int(dot_splitted[0])
            if len(dot_splitted) == 4:
                d['.'.join([dot_splitted[-2],dot_splitted[-1]])] = d.get('.'.join([dot_splitted[-2],dot_splitted[-1]]),0) + int(dot_splitted[0])
                d[dot_splitted[-1]] = d.get(dot_splitted[-1],0)+ int(dot_splitted[0])
            else:
                if len(dot_splitted)==3:
                    d[dot_splitted[-1]] = d.get(dot_splitted[-1],0)+ int(dot_splitted[0])
        for key in (d):
            temp = ' '.join([str(d[key]),key])
            result.append(temp)
        return (result)
