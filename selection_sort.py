def selection_sort(list_to_sort):
    comp = 0
    for i in range(len(list_to_sort)-1):
        min = i
        for j in range(i+1, len(list_to_sort)):
            comp += 1
            if list_to_sort[j] < list_to_sort[min]:
                min = j
        if min != i:
            swap(list_to_sort, i, min)
    return comp