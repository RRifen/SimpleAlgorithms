def quicksort(list):
    if (len(list) < 2):
        return list
    pivot = list[0]
    greater = [i for i in list[1:] if i > pivot]
    less = [i for i in list[1:] if i <= pivot]
    return quicksort(less) + [pivot] + quicksort(greater)
