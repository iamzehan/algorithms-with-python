def moveNumbers(array):
  i = 0 #current position
  j = 0 #next insert position
  while i<len(array):
    if array[i]!=0:
      val = array.pop(i)
      array.index(j, val)
      j+=1
    i+=1
  return array

if __name__ == '__main__':
    li = [0, 0, 3, 0, 12, 1, 0] #[3, 12, 1, 0, 0, 0, 0]
    result = moveNumbers(li)
    print(result)
    li = [3,0,1,21,12,0,0,2,13] #[3,1,21,12,2,13,0,0,0]
    result = moveNumbers(li)
    print(result)
    li = [0,1]
    result = moveNumbers(li)
    print(result)
  
