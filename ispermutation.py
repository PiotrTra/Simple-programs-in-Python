def ispermutation(tab1, tab2):
    i = 0
    j = 0
    z = 0
    sienna = " "
    for i in range(len(tab1)):
        for j in range(len(tab2)):
            if tab1[i] == tab2[j]:
                z += 1

    if z == len(tab1):
        print("True")
    else:
        print("False")


lista1 = [1, 2, 3, 6,10]
lista2 = [3, 2, 1, 4,12]
ispermutation(lista1, lista2)
