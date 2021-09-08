# # Brute force
from random import randint
def calcTargetSum(a, target):
    count = 0
    for i in range(0, len(a)):
        for j in range(i + 1, len(a)):
            count += 1
            if a[i] + a[j] == target:
                return count

    return count


def sum2(x, y):
    return x + y

def calcTargetSumBetter(a, target):
    a.sort()
    i = 0
    j = len(a) - 1
    count = 0
    while i < j:
        count += 1
        sumTarget = sum2(a[i], a[j])
        if sumTarget > target:
            j -= 1
        elif sumTarget < target:
            i += 1
        else:
            return count
    return count

res1 = []
for i in range(1000, 10000, 1000):
    a = [randint(0, 1000) for el in range(i)]
    target = randint(0, 10000)
    res1.append(calcTargetSum(a, target)/calcTargetSumBetter(a, target))

print(res1)
