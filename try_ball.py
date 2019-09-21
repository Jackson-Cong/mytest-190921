# -*- coding: UTF-8 -*-

#初始高度（m)
H0 = 100

#弹跳次数
times = 10

#第二次高度与第一次相比
rate = 0.5

#---------------------------------------------
#定义形成初始累加器
SUM = H0

Hn = H0 * rate
for n  in range(2, times + 1):
    SUM += 2 * Hn
    #print('No.%2d - Hn=%10f\tSUM=%f' % (n, Hn, SUM))
    print('No.%2d - Hn=%7.4f sum=%8.4f' % (n, Hn, SUM))
    Hn *= rate

print(SUM)
