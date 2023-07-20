numlist = [2,5,1,7,3,5]
print(numlist)
for i in range(len(numlist) - 1):
    for j in range(i + 1, len(numlist)):
        if numlist[i] > numlist[j]:
            tmp = numlist[i]
            numlist[i] = numlist[j]
            numlist[j] = tmp

print(numlist)