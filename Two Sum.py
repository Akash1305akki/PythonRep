N=int(input())
Val = str(input())
list_of_val=Val.split()
list_of_num = [int(x) for x in list_of_val]
S = int(input())
ans=[]

if(len(list_of_num)==N):
    for i in range(N):
        for j in range(i+1,N):
            I=list_of_num[i]
            J=list_of_num[j]
            if(I+J==S):
                ans.append(i)
                ans.append(j)
                break

print(ans)