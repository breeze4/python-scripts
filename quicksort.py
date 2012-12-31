#quick sort implementation

import random
import math
to_sort = range(0,60)
random.shuffle(to_sort)
print "list to be sorted: ", to_sort

def quicksortFun(elements):
        if len(elements) <= 1:
                return elements

        pivot = elements[0]
        less, greater = [],[]
        
        for item in elements[1:]:
                if item < pivot:
                        less.append(item)
                else:
                        greater.append(item)

        return quicksortFun(less) + elements[0:1] + quicksortFun(greater)


result = quicksortFun(to_sort)
print result
