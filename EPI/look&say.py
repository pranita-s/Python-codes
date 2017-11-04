import itertools

def look_and_say(n):
    s = '1'
    for _ in range(n-1):
        s = ((''.join(
            str(len(list(group)) + key for key,group in itertools.groupby(s)))))
    return (s)

answer = look_and_say(7)
print(''.join(answer))
for a in answer:
    print((a))

