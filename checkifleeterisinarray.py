def binary(arr, element):
    high = len(arr) - 1
    low = 0
    mid = 0

    while high >= low:
        mid = (high + low) // 2
        if arr[mid] > element:
            high = mid - 1
        elif arr[mid] < element:
            low = mid + 1
        else:
            return mid
    return -1


lista = [1, 3, 5, 10, 12, 15, 16]
liczba = 15

wynik = binary(lista, liczba)

if wynik != -1:
    print("nalezy do listy")
else:
    print("nie nalezy do listy")
