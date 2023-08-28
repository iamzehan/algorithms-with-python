def binary_search(array,item,high,low=0):
    mid = (high+low)//2
    guess = array[mid]
    if low<=high:
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
            return binary_search(array,item,high,low)
        else:
            low = mid + 1
            return binary_search(array,item,high,low)
    return None

array=[1,2,3,4,5,6]
print(binary_search(array,6,len(array)))
