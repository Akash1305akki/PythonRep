Val = str(input())
list_of_val = Val.split()

def bubble_sort(list_of_val):
    for i in range(len(list_of_val) - 1):
        for j in range(len(list_of_val) - i - 1):
            if list_of_val[j] > list_of_val[j + 1]:
                list_of_val[j], list_of_val[j + 1] = list_of_val[j + 1], list_of_val[j]
    return list_of_val

sorted_list = bubble_sort(list_of_val)

op = ' '.join(str(num) for num in list_of_val)
print(op)
