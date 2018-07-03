# TIME - O(n)

def countBinarySubstrings( s):
    if (len(s) == 0 or s.count('0') == len(s)
            or s.count('1') == len(s)):
        return 0

    counts = []
    cur = s[0]
    n_c = 0
    for c in s:
        if c == cur:
            n_c += 1
        else:
            counts.append(n_c)
            cur = c
            n_c = 1
    counts.append(n_c)

    ans = 0
    for i in range(1, len(counts)):
        ans += min(counts[i], counts[i - 1])
    return ans

print(countBinarySubstrings('101001'))
