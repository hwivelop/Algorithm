
index = 0
res_index = 0
res_max = 0

for i in range(9):

    x = int(input())
    if res_max < x:
        res_max = x
        res_index = i + 1

print(res_max)
print(res_index)
