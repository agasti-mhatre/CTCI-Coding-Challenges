def mergesort(x_list):
    if len(x_list) <= 1:
        return x_list

    left = mergesort(x_list[:(len(x_list)//2)])
    right = mergesort(x_list[(len(x_list)//2):])

    i = 0
    j = 0
    k = 0
    while (i < len(left)) and (j < len(right)):
        if left[i] <= right[j]:
            x_list[k] = left[i]
            i += 1
        else:
            x_list[k] = right[j]
            j += 1

        k += 1

    while i < len(left):
        x_list[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        x_list[k] = right[j]
        j += 1
        k += 1

    return x_list


def quicksort(x_list):
    if len(x_list) <= 1:
        return x_list
    
    pivot = x_list.pop()

    lt = []
    gt = []

    for item in x_list:
        if item <= pivot:
            lt.append(item)
        else:
            gt.append(item)

    return quicksort(lt) + [pivot] + quicksort(gt)


def countsort(x_list):
    if len(x_list) <= 1:
        return x_list

    min_ = min(x_list)
    max_ = max(x_list)
    list_ocurrences = []

    for i in range(min_, max_ + 1):
        list_ocurrences.append([i, 0])

    #print(list_ocurrences)
    #print("Min:", min_, "\t", "Max:", max_)

    for i in x_list:
        index = i - min_
        list_ocurrences[index][1] += 1


    j = 1
    while j < len(list_ocurrences):
        list_ocurrences[j][1] += list_ocurrences[j - 1][1]
        j += 1


    for j in range(len(list_ocurrences) - 1, 0 ,-1):
        list_ocurrences[j][1] = list_ocurrences[j - 1][1]
        if j == 1:
            list_ocurrences[0][1] = 0 


    i = 0
    k = 0
    while i < len(list_ocurrences):
        if i == (len(list_ocurrences) - 1):
            while k < len(x_list):
                x_list[k] = max_
                k += 1
            break
        elif list_ocurrences[i][1] != list_ocurrences[i + 1][1]:
            for a in range(list_ocurrences[i][1], list_ocurrences[i + 1][1]):
                x_list[k] = list_ocurrences[i][0]
                k += 1

        i += 1

    return x_list


'''def radixsort(x_list):
    if len(x_list) <= 1:
        return x_list

    min_length = int(len(str(min(x_list))))
    max_length = int(len(str(max(x_list))))
    
    y_list = []
    for num in x_list:
        y_list.append([num,num])


    for i in range(min_length, max_length + 1):
        list_ocurrences = []
        for a in range(0, 10):
            list_ocurrences.append([a, 0])

        for num in y_list:
            if abs(num[0]) < 10:
                ones_digit = num[0] % 10
            else:
                ones_digit = num[0] % 10

            list_ocurrences[ones_digit][1] += 1
            
            list_ocurrences[ones_digit].append(num[0])
            num[1] = num[1] // 10

        print(y_list)
        print(list_ocurrences)
        print()

'''



if __name__ == "__main__":
    #x_list = [3,9,2,1,3,5,1,7,5,6,3] # 1, 1, 2, 3, 3, 3, 5, 5, 6, 7, 9
    #x_list = [-1,-5,-3,7,8,9,10] # -5, -3, -1, 7, 8, 9, 10
    #x_list = [3,9,1,3,5,1,7,5,6,3] # 1, 1, 3, 3, 3, 5, 5, 6, 7, 9
    #print(countsort(x_list))
    
    x_list = [30,930,22,113,32,5,1,72,54,66,38]
    #radixsort(x_list)