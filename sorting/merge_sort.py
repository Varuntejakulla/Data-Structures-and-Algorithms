def dividing(nums:list):

    if len(nums)<=1:
        return nums

    mid = len(nums)//2

    left = nums[:mid]
    right= nums[mid:]

    left_arr = dividing(left)
    right_arr = dividing(right)

    return merge(left_arr,right_arr)


def merge(left_arr,right_arr):

    result =[]
    i,j=0,0
    n,m = len(left_arr),len(right_arr)

    while i<n and j<m:
        if left_arr[i]<right_arr[j]:
            result.append(left_arr[i])
            i+=1
        else:
            result.append(right_arr[j])
            j+=1

    while i<n:
        result.append(left_arr[i])
        i+=1

    while j<m:
        result.append(right_arr[j])
        j+=1

    return result

nums=[9, 12, 18, 25, 27, 31, 38, 43]
print(dividing(nums=nums))
