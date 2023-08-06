import numpy as np
for i in range(8):
    offset = np.array([(i >> 0) & 1, (i >> 1) & 1, (i >> 2) & 1])
    print(offset)
print(4&1)
print(4>>3)#4的二进制表达为00000100全部右移3位00000000输出为0





