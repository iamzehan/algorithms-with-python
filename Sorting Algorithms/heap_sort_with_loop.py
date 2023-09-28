# This is the OG of sorting algorithms that was invented back in the 1960s! Mind boggling yet once you get it, it becomes simpler with every try!
def heapify(arr, n, i):
    while True:
        root = i
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        if left_child < n and arr[root] < arr[left_child]:
            root = left_child

        if right_child < n and arr[root] < arr[right_child]:
            root = right_child

        if root == i:
            break

        arr[i], arr[root] = arr[root], arr[i]
        i = root

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
