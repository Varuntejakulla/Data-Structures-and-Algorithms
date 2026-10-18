def selection_sort(nums):
    n=len(nums)
 
    for i in range(0,n):
        min_index=i
        for j in range(i+1,n):
            if nums[min_index]>nums[j]:
                min_index =j
        nums[i],nums[min_index]=nums[min_index],nums[i]
    return nums

nums=[1,3,5,4,6,8]

print(selection_sort(nums=nums))



def disorder_selction_sort(nums:list):
    n = len(nums)
    for i in range(n-1,0,-1):
        max_index = i
        for j in range(i):
            if nums[max_index] < nums[j]:
                max_index =j
        nums[i],nums[max_index] = nums[max_index],nums[i]
    return nums
nums = [1, 3, 1,3, 6, 8]

print(disorder_selction_sort(nums=nums))



nums = [1, 100, 1,3, 7, 8]

def recursion_sort(nums):

    def find_min(nums,j,min_index):
        if j == len(nums):
            return min_index

        if nums[j]<nums[min_index]:
            min_index =j

        return find_min(nums,j+1,min_index)

    def sort(nums,i):
        if i==len(nums)-1:
            return 
        min_index= find_min(nums,i+1,i)

        nums[i], nums[min_index] = nums[min_index], nums[i]

        sort(nums,i+1)
    sort(nums,0)

    return nums

print(recursion_sort(nums=nums))

























