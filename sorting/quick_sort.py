def partion(nums,low,high):
    pivot = nums[low]

    i,j=low,high

    while  i<j:

        while nums[i]<=pivot and i<=high-1:
            i+=1

        while nums[j]>
