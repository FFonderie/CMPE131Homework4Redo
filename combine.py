def combine_lists(list1, list2):

    list1 += list2

    #insertion sort because I am on time crunch
    for i in range(1,len(list1)):
        key = list1[i]
        if (type(key) != int):
            raise TypeError("only integers allowed")
        j = i - 1

        while (j >= 0 and key > list1[j]):
            list1[j+1] = list1[j]
            j -= 1
        list1[j+1] = key

    #ultra lazy implementation
    i = 0
    while (i < len(list1) - 1):
        if (list1[i] == list1[i+1]):
            del list1[i+1]
        else:
            i += 1
        

    
    return list1


