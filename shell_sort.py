def shell_sort(arr):
    gap = len(arr)//2
    while gap>0:
        for i in range(gap, len(arr)):
            key = arr[i]
            j = i
            while j>=gap and arr[j-gap]>key:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = key
        gap = gap//2
    return arr

print(shell_sort([4,1,9,3,8,2,7,6]))
