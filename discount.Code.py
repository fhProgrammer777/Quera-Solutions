n, t = input().split()
n = int(n)
for i in range(n):
    s = input()
    flag = True
    for s_char in s:
        flag1 = False
        for t_char in t:
            if s_char == t_char:
                flag1=True
        if not flag1:
            flag = False
    for t_char in t:
        flag1 = False
        for s_char in s:
            if s_char == t_char:
                flag1 = True
        if not flag1:
            flag = False
    if flag:
        print("Yes")
    else:
        print("No")
