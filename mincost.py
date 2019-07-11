dat1,dat2=input().split()
c=abs(len(dat2)-len(dat1))
for g in range(len(dat1)):
  if(len(dat2)==1 and dat2[g] in dat1):
    break
  if(dat1[g]!=dat2[g]):
    c=c+1
print(c)
