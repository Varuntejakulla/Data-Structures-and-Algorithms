def bubble_sort(nums):

    n=len(nums)

    for i in range(n):
        for j in range(0,n-i-1):
            if nums[j]>nums[j+1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums 



def bubble_sort_optii(nums):
    n=len(nums)
    for i in range(n):
        swapped = False

        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True

        if  not swapped:
            break
    return nums 


nums=[378,524,2,3,2,234,43,1]


print(bubble_sort(nums))
print(bubble_sort(nums))