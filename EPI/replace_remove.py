def replace_and_remove(size,s):
    write_idx,a_count = 0,0
    for i in range(size):
        if s[i]!= 'b':
            s[write_idx] = s[i]
            write_idx += 1
        if s[i] == 'a':
            a_count += 1

    cur_idx = write_idx - 1
    write_idx += a_count - 1
    final_size = write_idx + 1
    while cur_idx >= 0:
        if s[cur_idx] == 'a':
            s[write_idx - 1:write_idx + 1] = ['d','d']
            write_idx -= 2

        else:
            s[write_idx] = s[cur_idx]
            write_idx -= 1

    cur_idx -= 1
    return final_size

s = ['a','c','d','b','b','c','a']
#s= 'acdbbca'
print(replace_and_remove(7,s))