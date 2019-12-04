# Part 1
ans_l = []
ans = 0
for n in range (284639, 748756):
    n_str = str(n)
    if len(set(n_str)) == len(n_str):
        continue
        
    adj = False
    dec = False
    i = 0
    for i in range(i, 6):
        for y in range(i+1, 6):
            if n_str[i] == n_str[y] and y == i + 1:
                adj = True
            if n_str[i] > n_str[y]:
                dec = True
                break
        if dec:
            break
        i += 1

    if adj and not dec:
        ans_l.append((n))
        ans += 1

print(ans)


# Part 2

def x(n):
    two = False
    for i in range(10):
        ans = str(n).count(str(i))
        if ans == 2:
            two = True
            break
    return two


c = 0

for i in ans_l:
    if x(i):
        c +=1

print(c)

            
        
