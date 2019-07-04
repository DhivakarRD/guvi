num1=int(input())
if (num1%4)==0:
  if(num1%100)==0:
    if(num1%400)==0:
      print('yes')
    else:
      print('no')  
  else:
    print('yes')
else:
  print('no')
