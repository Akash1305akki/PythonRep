Val = str(input())
list_of_val=Val.split()
list_of_num = [int(x) for x in list_of_val]

for i in range(len(list_of_num)):
    I=list_of_num[i]
    count=list_of_num.count(I)
    if(count==1):
        print(I)