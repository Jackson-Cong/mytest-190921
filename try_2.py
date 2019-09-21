# -*- coding: UTF-8 -*-
# sum of natural number

import fractions

num_start = 1
num_end = 10000

sum = 0
for num in range (num_start, num_end + 1):
    #fc = 1 / num
    fc = fractions.Fraction(1, num)
    sum += fc
    print('add %s to summaary, then sum=%s' %(fc, sum) )

print(sum)
