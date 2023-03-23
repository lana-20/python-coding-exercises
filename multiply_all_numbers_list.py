# Input:  list1 = [3, 2, 4]
# Output: 24
# Explanation: 3 * 2 * 4 = 24

# Approach 1: Traversal
mylist = [3, 2, 4]
# result = 1

# for x in mylist:
#     result = result * x     # 3->6->24


# Approach 2: numpy.prod()  * Install numpy package
import numpy
result = numpy.prod(mylist)


print(result)