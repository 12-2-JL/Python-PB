N, K=5, 3
DiamondsSize=[1, 6, 4, 3, 1]
DiamondsSize.sort()
DiamondsDisplayed=0

for i in range(N):
    j=0
    while DiamondsSize[i]-DiamondsSize[j]>K:
        j+=1
    DiamondsDisplayed=max(DiamondsDisplayed, i-j+1)


print(DiamondsDisplayed)