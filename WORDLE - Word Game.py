S=str(input())
T=str(input())
arr=[]
N=len(S)

for i in range(0,N):
    if(S[i]==T[i]):
        arr.append('G')
    else:
        arr.append('B')

ans=''.join(arr)
print(ans)
