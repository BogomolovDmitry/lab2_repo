def str_reverse(pstr):
  result = ""
  for i in range(len(pstr)):
    result = pstr[i] + result
  return result
str1 = "hello, world"
print(str_reverse(str1))