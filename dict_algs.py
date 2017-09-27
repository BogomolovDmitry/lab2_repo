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


test(emps)    
