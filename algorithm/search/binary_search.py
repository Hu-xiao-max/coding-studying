#二分查找查找的是索引，所以在使用递归调用的时候需要传入索引的参数来控制递归的传入传出
# 以下代码的核心就是把开始和结束的索引作为input的parameter来递归
def bs(arr,start,end,target):
    mid=int(start+(end-start)/2)
    if arr[mid]==target:
        return mid
    elif arr[mid]<target:
        return bs(arr,mid,end,target)
    else:
        return bs(arr,start,mid,target)
arr = [ 2, 3, 4, 10, 40 ] 
target = 10
print(bs(arr,0,len(arr)-1,target))



