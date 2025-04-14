c=0
x=int(input())
for i in range(1,x**2+1):
    n=x-i**2
    k=n**0.5
    if n>0 and int(k)==k:
        c+=1
print(c//2)
