def get_min(arr):
    if len(arr) == 0:
      return -1
    minimum = arr[0]
    for value in arr:
      current = value
      if current < minimum:
        minimum = current
    return minimum
  
  
def get_avg(arr):
  if len(arr) == 0:
      return -1
  summ = 0
  for i in range(len(arr)):
    summ += arr[i]
  return summ / len(arr)


def str_reverse(pstr):
  result = ""
  for i in range(len(pstr)):
    result = pstr[i] + result
  return result  


def check_age(children):
  yest_18 = False
  for child in children:
    if child['age'] > 18:
      yest_18 = True
  return yest_18


def test(emps):
  for value in emps:
    if check_age(value.get('children', ())):
      print(value['name'])
      break

def main():
  arr1 = []
  print(get_min(arr1))  
  arr2 = [2, 2, 4, 4]     
  print(get_avg(arr2))
  str1 = "hello, world"
  print(str_reverse(str1))
  ivan = {
    "name" : "ivan" ,
    "age" : 34 ,
    "children" : [{
      "name" : "vasja" ,
      "age" : 32 ,
      }, {
      "name" : "petja" ,
      "age" : 19 ,
                }],
          }
  darja = {
    "name" : "darja" ,
    "age" : 41 ,
    "children" : [{
      "name" : "kirill" ,
      "age" : 11 ,
      }, {
      "name" : "pavel" ,
      "age" : 15 ,
                }],
          }
  emps = [ ivan , darja]
  test(emps)

print(__name__)
if __name__=='__main__':
   main()