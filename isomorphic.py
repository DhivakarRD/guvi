num1,num2=map(str,input().split())
if(len(num1)!=len(num2)):
    print("no")
else:
  a=[num1.count(i) for i in num1]
  b=[num2.count(i) for i in num2]

if(a==b):
    print("yes")
else:
    print("no")
