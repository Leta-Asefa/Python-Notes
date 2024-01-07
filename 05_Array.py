import array as Array            # to decrease naming conflict in larger projects don't use from array import *
from math import sqrt
from numpy import *

nums =Array.array('i',[1,2,3,4,5,6,7,8,9])
print(nums.typecode)
nums.reverse()
for num in nums:
    print(num)

copiedArray=Array.array(nums.typecode,(a for a in nums))
for element in copiedArray:
    print(element)


print(sum(nums))
print(min(nums))
print(max(nums))
print(concatenate(nums,copiedArray))

