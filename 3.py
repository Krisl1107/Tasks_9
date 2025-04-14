N=int(input())
K=[]
for i in range(2,1000):
    if N%i==0:
        print(i)
        break
    else:
        continue
