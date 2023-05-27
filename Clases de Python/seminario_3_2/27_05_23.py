# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

# arrOfNumbers = [1, 1, 2, 0, -1, 3, 4, 4]
# print(len(set(arrOfNumbers)))

"""
newArrOfNumbers = set()
for i in range(arrOfNumbers):
    newArrOfNumbers.add(arrOfNumbers[i])
print(newArrOfNumbers)
"""
# Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо,  K – положительное число.
# Input:   [1, 2, 3, 4, 5] k = 3
# Output:  [3, 4, 5, 1, 2]
"""
lst = [1, 2, 3, 4, 5]
k = 3

for i in range(k):
    num = lst.pop(-1)
    lst.insert(0, num)

print(lst)
"""
# Напишите программу для печати всех уникальных значений в словаре. 
# Input:  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}] 
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

ceys = dict()
ceys = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]

text = []
text_set = set()
for item in ceys:
    text.append(*item.values()) 
    text_set.add(*item.values())
print(text, text_set)