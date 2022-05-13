lista = [[1,0,0,1],[1,1,1,1],[0,0,0,1]]
xyz = 0

for i in range(len(lista)):
    max = 0
    for j in range(len(lista[i])):
        if lista[i][j] == 1:
            max += 1
    if xyz < max:
        xyz = max
if max == 0:
    print("-1")
else:
    print(xyz)
