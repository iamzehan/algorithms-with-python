# We have practiced selection sort, now let's make the space complexity a bit better, O(1)
def inline_selection_sort(array):
    for i in range(0,len(array)):
        j = array.index(min(array[i:]))
        minimum = array[j]
        current = array[i]
        if j > i:
            array[i] = minimum
            array[j] = current
        elif j ==i:
            continue
    return array
