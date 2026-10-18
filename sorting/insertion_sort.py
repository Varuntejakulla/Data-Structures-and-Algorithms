def insertion_sort(nums:list):
    n=len(nums)

    for i in range(1,n):
        key = nums[i]
        j=i-1

        while j>=0 and nums[j]>key:
            nums[j]=key
            j-=1


        nums[j+1]=key
    return nums


nums=[2,4,2,4,2,4,5]

print(insertion_sort(nums))

