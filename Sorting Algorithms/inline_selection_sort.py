def inline_selection_sort(array):
    for i in range(0,len(array)):
        j = array.index(min(array[i:]))
        if j > i:
            array[i],array[j]=array[j],array[i]
        elif j ==i:
            continue
    return array
print(inline_selection_sort([2,7,3,5,1,4]))
