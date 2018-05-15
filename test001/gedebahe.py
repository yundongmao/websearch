class Solution(object):
    def __init__(self):
        return
    def getPrimeList(self,N):
        a = [0]*N
        for i in range(2,N):
            for j in range(2*i,N,i):
                a[j]=1
        return [i for i in range(len(a)) if a[i] ==0][2:]
a = Solution()
primeL = a.getPrimeList(100000)
primeSet =  set(primeL)
print primeL
for k in primeL[:1000]:
    for i in range(6,100000,2):
        for j in primeL:
            if i-j in primeSet:
                if j<=k:
                    # print i,j,i-j
                    break
        else:
            print k,k*k,i
            break
    else:
        break
