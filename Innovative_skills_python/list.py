#   1D list : multipul colam thake

# product_name = ["chicken", "egg", "salt"]
# size_product_name_list = len(product_name)
# print(size_product_name_list)
# print(product_name[size_product_name_list-1])

# for i in range(size_product_name_list):
#     print(product_name[i])


# 2D liat : multipul row thake 

# x = [[1,2,3,4], [5,6,7,8], [9,10,11,12],[13,14,15,16]]

# for i in range(len(x)):
#     row = x[i]
#     row_sum = sum(row)
#     row_avg = row_sum / len(row)

#     for val in row:
#         print(val, end=" ")
#     print(row_avg)

import math

x = [[1,2,3,4,5,6], 
     [5,6,7,8,6,7],
     [9,10,11,12,7,8],
     [13,14,15,16,8,9],
     [16,17,18,19,9,10]] 


col = len(x[0])
row = len(x)


row_sum_list = []

for i in range(row):
    row_sum = 0
    for j in range(col):
        row_sum += x[i][j]
        row_sum_avg =  row_sum/col
    row_sum_list.append(row_sum_avg)


total_avg = 0

for i in range(len(row_sum_list)):
    total_avg += row_sum_list[i]

for i in range(row):
    for j in range(col):
     mean_row = (col/2)+1   
     round_mean = math.ceil(mean_row)
     x[i][round_mean] = total_avg
     print(f"{x[i][j]:5.2f}", end=" ")
    print()
    
    
     

























































































































































































































































































