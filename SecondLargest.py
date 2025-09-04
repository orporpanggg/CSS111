nums = [5, 5, 5, 4]
print(nums)

nums_2 = []
for number in nums:
    if number not in nums_2:
        nums_2.append(number)

if len(nums_2) < 2:
    print("None")
else:
    max1 = float('-inf')
    max2 = float('-inf')
    for number in nums_2:
        if number > max1:
            max2 = max1
            max1 = number
        elif number > max2 and number != max1:
            max2 = number
    if max2 == float("-inf"):
        print("None")
    else:
        print(max2)