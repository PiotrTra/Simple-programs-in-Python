def replace(d, v, e):
    for key,val in d.items():
        if val == v:
            d[key] = e


    print(d)


replace({1: 2, 13: 12, 2: 4, 3: 2, 5: 2}, 2, 7)
