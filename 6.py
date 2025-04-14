for ab in range(10,100):
    n=ab**2
    k=n%100
    if k==ab and ab**2<1000:
        print(ab*ab)
