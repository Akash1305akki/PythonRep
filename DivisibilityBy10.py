Num=int(input())
Val = str(input())
list_of_val = Val.split()
last_char = [word[-1] for word in list_of_val]

store = ''.join(str(num) for num in last_char)
STORE = int(store)

if STORE % 10 == 0:
    print("Yes")
else:
    print("No")
