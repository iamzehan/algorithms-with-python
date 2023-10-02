# This is the OG of sorting algorithms that was invented back in the 1960s! Mind boggling yet once you get it, it becomes simpler with every try!
# Time complexity for it is O(n log(n)) and space complexity is O(1)
def heapify(arr, n, i):
  # Find largest among root and children
  root = i
  l = 2 * i + 1
  r = 2 * i + 2

  if l < n and arr[root] < arr[l]:
      root = l

  if r < n and arr[root] < arr[r]:
      root = r

  # If root is not the largest, then swap with the largest and continue heapifying
  if root != i:
      # swap
      arr[i], arr[root] = arr[root], arr[i]
      # continue 
      return heapify(arr, n, root) 
  else: # if root is the largest element in the tree then return the array
    return arr

def heapSort(arr):
  n = len(arr)

  # Build max heap
  for i in range(n//2, -1, -1):
      arr = heapify(arr, n, i)

  for i in range(n-1, 0, -1):
      # Swap
      arr[i], arr[0] = arr[0], arr[i]

      # Heapify root element
      arr = heapify(arr, i, 0)
  return arr
  
if __name__ == '__main__':
  arr = [6,3,10,12,9,5,11,2,7,4,1,8] 
  print(heapSort(arr)) # >> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
  arr = [1, 12, 9, 5, 6, 10]
  print(heapSort(arr)) # >> [1, 5, 6, 9, 10, 12]
