run = []
k4 = str()
for k in range (100000,999999):
    N=k
    k1=str(k)[1:]
    k2=N+1
    k2_=str(k2)[1:]
    k3=N+2
    k3_=str(k3)[1:][:-1]
    k4=N+3
    k4_=str(k4)
    if k1==k1[::-1] and k2_==k2_[::-1] and k3_==k3_[::-1] and k4_==k4_[::-1]:
        run.append(N)
print (run)
