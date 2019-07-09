
numb1,numb2=map(int,input().split())
ct=0
for i in range(num1,num2+1):
    if(i > 1):
        for j in range(2,i):
            if((i%j)==0):
                break
        else:
            ct=ct+1

print(ct)
