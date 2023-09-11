def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr

unsorted_array = [67, 12, 45, 89, 34, 56, 78, 23, 90, 1, 55, 33, 77, 9, 41, 88, 60, 19, 73, 7]
print(insertion_sort(unsorted_array))
