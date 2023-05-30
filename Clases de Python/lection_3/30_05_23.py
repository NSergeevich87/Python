"""
#  ФУНКЦИЯ!
"""
def sum_numbers(n, y = 'hello!'):
    print(y)
    summa = 0
    for i in range(1, n+1):
        summa += i
    return summa

print(sum_numbers(5, 'adios'))

def sum_str(*args):
    res = ''
    for i in args:
        res += str(i)
    return res

print(sum_str(1, 2, 3, 4, 5))
"""
# РЕКУРСИЯ
"""
# Фибоначчи
def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n-1) + fib(n-2)

list_1 = []
for i in range(1, 10):
    list_1.append(fib(i))
print(list_1)

# Быстрая сортировка!
def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort([98,7,6,5,34,56,7,8,9,87,5,67,6]))

# Сортировка делением пополам!
def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

list_2 = [87,5,6,97,8,86,43,58,76]
merge_sort(list_2)
print(list_2)