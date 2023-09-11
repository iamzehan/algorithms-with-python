import random
def quick_sort(array):
    if len(array)<2:
        return array
    else:
        idx = random.randint(0, len(array)-1) #picking a random index every time
        print(idx)
        pivot = array[idx]
        less = [i for i in array[:idx]+array[idx+1:] if i<= pivot]
        greater = [i for i in array[:idx]+array[idx+1:] if i > pivot]
        return quick_sort(less)+[pivot]+quick_sort(greater)

print(quick_sort([5,10,3,2,7,11,4,1,9]))
