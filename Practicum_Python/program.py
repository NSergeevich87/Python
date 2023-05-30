i = 0
nums = list()
while i < 5:
    nums.append(int(input()))
    i += 1
sum_ = 0
for i in range(len(nums)):
    sum_ += abs(nums[i])
print(sum_)