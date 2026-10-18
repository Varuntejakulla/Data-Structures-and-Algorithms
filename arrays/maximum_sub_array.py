def maximum_subarray(nums):

    n= len(nums)
    maxi = float("-inf")

    for i in range(0,n):
        total =0
        for j in range(i,n):

            total =total+nums[j]
            maxi =max(maxi,total)
    return maxi 

def max_subarray(nums:list):
    sub_arr =[]
    n=len(nums)
    maxi  = float("-inf")
    total =0
    for i in range(0,n):
        total =total+nums[i]
        maxi =max(maxi,total)
        sub_arr.append(nums[i])
        if total<0:
            sub_arr.remove(nums[i])
            total=0
    return maxi,sub_arr


nums=[1,2,3,-1,5,1,4,6,8,9]
print(max_subarray(nums=nums))