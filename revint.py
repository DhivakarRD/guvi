data=int(input())
revdata=''
while data>0:
  lastdigit=data%10
  revdata=revdata+str(lastdigit)
  data=data//10
print(revdata)
