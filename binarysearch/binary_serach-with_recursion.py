
def binary_serach(nums:list,target):
    nums.sort()
    low=0
    high = len(nums)-1

    def binary_searchin_with_reccursion(nums,low,high,target):
        if low >high:
           return -1
        mid = (low+high)//2
        if nums[mid]== target:
            return mid
        elif nums[mid]<target:
            return binary_searchin_with_reccursion(nums,mid+1,high,target)
        else:
            return binary_searchin_with_reccursion(nums,low,mid-1,target)
    return binary_searchin_with_reccursion(nums,low,high,target)

nums =[2,4,5,3,2,4,5]

target =5

print(binary_serach(nums=nums,target=target))



