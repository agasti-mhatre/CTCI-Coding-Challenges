def mergeAB(a, b):
    x = []

    i = 0
    j = 0
    while (i < len(a)) and (j < len(b)):
        if a[i] <= b[j]:
            x.append(a[i])
            i += 1
        else:
            x.append(b[j])
            j += 1

    while i < len(a):
        x.append(a[i])
        i += 1

    while j < len(b):
        x.append(b[j])
        j += 1

    a = x[:]

    return a



if __name__ == "__main__":
    a = [1, 2, 3, 3, 5, 10]
    b = [4, 6, 11, 17]

    print(mergeAB(a, b))