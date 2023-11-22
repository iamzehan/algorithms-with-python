def moveNumbers(array):
  left = 0
  right = 1
  while right<len(array):
    if array[left]!=0:
      left+=1
    array[left], array[right] = array[right], array[left]
    right+=1
  return array

if __name__ == '__main__':
    li = [0, 0, 3, 0, 12, 1, 0] #[3, 12, 1, 0, 0, 0, 0]
    result = moveNumbers(li)
    print(result)
    li = [3,0,1,21,12,0,0,2,13]
    result = moveNumbers(li)
    print(result)
    li = [0,1]
    result = moveNumbers(li)
    print(result)
