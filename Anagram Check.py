Val = str(input())
list_of_val = Val.split()
word_1=list_of_val[0]
word_2=list_of_val[1]
new1= list(word_1)
new2= list(word_2)
new1.sort()
new2.sort()


if len(new1) == len(new2):
    for i in range(len(new1)):
        if new1[i] != new2[i]:
            print("No")
            break
    else:
        print("Yes")