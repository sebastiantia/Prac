def selection_sort(list):
    for i in range(len(list)):
        minIdx = i
        for j in range(i, len(list)):
            if list[j] < list[minIdx]:
                minIdx = j

        temp = list[minIdx]
        list[minIdx] = list[i]
        list[i] = temp
        print(list)

    return list
        
list = [4,5,6,1,2,3]


selection_sort(list)



    