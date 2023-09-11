def quick_sort(array):
    if len(array)<2:
        return array
    else:
        mid = len(array)//2 # taking middle index as pivot
        pivot = array[mid]
        less = [i for i in array[:mid]+array[mid+1:] if i<= pivot]
        greater = [i for i in array[:mid]+array[mid+1:] if i > pivot]
        return quick_sort(less)+[pivot]+quick_sort(greater)

print(quick_sort([5,10,3,2,7,11,4,1,9]))
