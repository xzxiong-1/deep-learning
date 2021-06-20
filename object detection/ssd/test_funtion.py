# rasier funtion test 

import itertools
for i, j in itertools.product(range(5), repeat=2):  # i -> 行（y）， j -> 列（x）
                    # 计算每个default box的中心坐标（范围是在0-1之间）
                    print(i, j)  #移到中心