import functools
import string

def s_to_i(s):
    return functools.reduce(lambda running_sum,
                            c:running_sum * 10 + string.digits.index(c),
                            s[s[0] == '-':],0) * (-1 if s[0] == '-' else 1)

print(s_to_i('34543'))