from itertools import groupby

data =list(input())

# Grouping adjacent duplicates
groups = groupby(data)
answer=''
for key, group in groups:
    w=f'{len(list(group)),int(key)}'
    answer+=w+' '
print(answer.strip())

