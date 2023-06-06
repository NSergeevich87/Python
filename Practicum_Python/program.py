n = int(input())
old_list = list()
for i in range(n):
    old_list.append(int(input()))

new_list = sorted(old_list)
print(new_list)
print(max(new_list))

flag = False

for i in new_list:
    while flag == False:
        if new_list[-i] < max(new_list):
            print(new_list[-i])
            flag = True
