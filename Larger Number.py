def largest_number(numbers):
    numbers = [str(x) for x in numbers]
    numbers.sort(key=lambda x: x * (9 // len(x) + 1), reverse=True)
    return int(''.join(numbers))

Val = str(input())
list_of_val=Val.split()
numbers = [int(x) for x in list_of_val]
N=len(numbers)

result = largest_number(numbers)
print(result)
