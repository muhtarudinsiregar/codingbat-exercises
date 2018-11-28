import time
from random import randrange

def findMin(aList):
    overallMin = aList[0]
    for i in aList:
        if i < overallMin:
            overallMin = i
    return overallMin

# print(findMin([5,3,0]))

for listSize in range(10000, 10001, 1000):
    aList = [randrange(100000) for x in range(listSize)]
    start = time.time()
    print(findMin(aList))
    end = time.time()
    print("size: %d time %f" % (listSize, (end-start)))
