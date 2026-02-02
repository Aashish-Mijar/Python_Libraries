list1 = [2,5,6,7]
list2 = [9,8,3,1]

result = [x+y for x, y in zip(list1, list2)]
print(result)


# operation applies in entire array
# 100 times faster than loops
