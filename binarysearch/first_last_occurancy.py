def first_last_oocurancy(nums:list,traget):

    first_time = -1
    last_time = -1


    low =0
    high = len(nums)-1

    while low <high:

         mid = high+low //2

         if nums[mid]==traget:
               first_time = mid
               high = mid - 1

         elif nums[mid]<traget:

              low = mid+1
              last_time = mid

         else:
              high = mid-1
              last_time = mid


    return  [first_time,last_time]


nums=[1,2,3,4,5,5,6,6,6,6,7,8]


print(first_last_oocurancy(nums=nums,traget=5))


