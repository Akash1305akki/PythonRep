Val = str(input())
list_of_val = Val.split()
list_of_num = [int(x) for x in list_of_val]
M=list_of_num[0]
N=list_of_num[-1]
count=0

for i in range(M,N+1):
    for j in range(2,i+1):
        if(i%1==0)and(i%j==0):
            if(i!=j):
                break
            count=count+1


print(count)
