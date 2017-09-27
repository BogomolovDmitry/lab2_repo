def get_min(arr):
    if len(arr) == 0:
      return -1
    minimum = arr[0]
    for value in arr:
      current = value
      if current < minimum:
        minimum = current
    return minimum
arr1 = []
print(get_min(arr1))   
  
def get_avg(arr):
  if len(arr) == 0:
      return -1
  summ = 0
  for i in range(len(arr)):
    summ += arr[i]
  return summ / len(arr)
arr2 = [2, 2, 4, 4]     
print(get_avg(arr2))