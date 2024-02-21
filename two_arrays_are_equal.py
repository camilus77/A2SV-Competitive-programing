#Two array are different
def check(self,A,B,N):
    #code here
    a=list(A)
    b=list(B)
    a.sort()
    b.sort()
    c=[a[i]-b[i] for i in range(len(a)) if a[i]-b[i]!=0]
    if c:
        return False
    else:
        return True