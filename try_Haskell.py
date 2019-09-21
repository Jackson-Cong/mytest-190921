# -*- coding: UTF-8 -*-


max_num = 10

fname = 'Haskell.txt'
f = open(fname,'w')

for a in range(1, max_num):
    data = ''
    for b in range(1, max_num):
        c = a * b
        if a>=b:
            print('%dx%d=%2d\t' % (b,a,c), end ='')
            data += '%dx%d=%2d\t' % (b,a,c)

    print('\n')
    #写入文件
    data+='\n'
    f.write(data)

f.close()
