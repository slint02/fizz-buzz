n = int(1)
for i in range(1, 100,1):
    n = i % 3 
    if n == 0: 
      print('not-fizz')
    else:
      print('fizz')
    n =  i % 5 
    if n == 0:
      print('not-buzz')
    else:
      print('buzz') 
