from re import L
import sys
from exception import Lab5Exception
# def rotate(arr):

#     rotated_array = []
#     print(len(arr))
#     for j in (len(arr[0])-1,0,-1):
#         l=[]
#         for i in range(int(len(arr))):
#              #rotated_array[len(arr)-j].append(arr[i])
#              l.append(arr[i][j])
#         rotated_array.append(l)
#     return rotated_array
def rotate(num):
    # for row in num:
    #     for i in range(len(row)):
    #         print(row[i])
    if(type(num))!=list:
         raise Lab5Exception("Exception Occured: Incorrect type")
    ans_list = []
    intermediate_list = []
    i=0
    while(i<len(num)):
        if(len(num)!=len(num[i])):
            raise Lab5Exception("Exception Occured: Incorrect dimensions")
        i=i+1

    for j in reversed(range(len(num))):
        for i in range(len(num)):
            intermediate_list.append(num[i][j])
        ans_list.append(intermediate_list)
        intermediate_list = []
    return ans_list