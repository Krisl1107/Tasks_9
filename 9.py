N=int(input())
k=0
for i in range(N+1):
    for j in range(i,N+1):
        k+=i+j
print(k)
