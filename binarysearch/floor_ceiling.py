def floor_ceil(nums,traget):

     floor =-1
     ceil = -1

     low = 0
     high = len(nums)-1

     while low<=high:

          mid = (low+high)//2
          
          if nums[mid]==traget:
               floor =nums[mid]
               ceil = nums[mid]
               break

          elif nums[mid]>traget:
               ceil = nums[mid]

               high =mid-1
               

          else:
               floor = nums[mid]

               low =mid+1


     return [floor, ceil]

print(floor_ceil([1, 2, 4, 6, 8, 10], 5))
