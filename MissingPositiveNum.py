def missing_positive(val):
    n = len(val)
    for i in range(n):
        if (abs(val[i]) - 1 < n and val[abs(val[i]) - 1] > 0):
            val[abs(val[i]) - 1] = -val[abs(val[i]) - 1]

    for i in range(n):
        if val[i] > 0:
            return i + 1

    return i + 1

Val = str(input())
list_of_val = Val.split()

val = [int(x) for x in list_of_val]
missing = missing_positive(val)
print(missing)