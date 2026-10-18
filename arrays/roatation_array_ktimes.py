def roating_array_ktimes(nums:list,k):

    n=len(nums)
    roations= k%n

    for _ in range(roations):
        e=nums.pop()
        nums.insert(0,e)
    return nums


nums=[2,2,4,2,4,2,4]
print(roating_array_ktimes(nums=nums,k=10))



# k=3
# def reverse(nums,left,right):
#     while left<right:
#         nums[left],nums[right]=nums[left],nums[right]
#         left+=1
#         right+=-1

# reverse(nums,n,)

def  roataions_of_array(nums:list,k):
    roatations = k%(len(nums))
    for _ in range(nums):
        e=nums.pop()
        nums[0]= nums.insert(e)

    return nums

nums=[2,2,4,2,4,2,4]
print(roating_array_ktimes(nums=nums,k=10))
