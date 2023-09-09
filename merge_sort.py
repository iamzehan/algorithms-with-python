#Let's code merge sort
def merge_sort(arr):
  if len(arr)>1:
    mid = len(arr)//2
    
    L = arr[:mid]
    R = arr[mid:]

    #first we sort left side
    merge_sort(L)
    # then right side
    merge_sort(R)

    # The below are index of L, R, and Main arr in the same order
    i = j = k = 0

    #looping through the two lists at the same time
    while i < len(L) and j < len(R):
      if L[i] <= R[j]:
        arr[k] = L[i] # adding to the main list
        i += 1
      else:
        arr[k] = R[j]
        j += 1
      k +=1

    #checking for remainings
    while i < len(L):
      arr[k] = L[i]
      i += 1
      k += 1
    while j < len(R):
      arr[k] = R[j]
      j +=1
      k +=1
  else:
    return arr

arr = [54,26,93,17,77,31,44,55,20]
merge_sort(arr)
print(arr) # >> [17, 20, 26, 31, 44, 54, 55, 77, 93]

# © this code was taken from geeksforgeeks merge sort tutorial under python3 code block.
