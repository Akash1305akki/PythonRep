Val = str(input())
list_of_val = Val.split()
list_of_num = [int(x) for x in list_of_val]
M=list_of_num[0]
N=list_of_num[-1]
count=0

for i in range(M,N+1):
    if(i%10==2):
        count=count+1
    elif(i%10==3):
        count=count+1
    elif(i%10==9):
        count = count + 1

print(count)