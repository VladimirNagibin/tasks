n = 10
m = 9
ind = 1
res_list = [['' for _ in range(m)] for _ in range(n)]
left_right = True
top_bottom = True
horizontally = True

for i in range(1, m + n):
    if horizontally:
        if left_right:
            num = int((i - 1) / 4)
            for j in range(num, m - num):
                res_list[num][j] = ind
                ind += 1
            left_right = False
        else:
            num = int((i - 3) / 4)
            for j in reversed(range(num + 1, m - num)):
                res_list[n - num - 1][j - 1] = ind
                ind += 1
            left_right = True
        horizontally = False
    else:
        if top_bottom:
            num = int((i - 2) / 4)
            for j in range(num, n - num - 1):
                res_list[j + 1][m - num - 1] = ind
                ind += 1
            top_bottom = False
        else:
            num = int((i - 4) / 4)
            for j in reversed(range(num + 1, n - num - 1)):
                res_list[j][num] = ind
                ind += 1
            top_bottom = True
        horizontally = True
for str in res_list:
    print(str)
