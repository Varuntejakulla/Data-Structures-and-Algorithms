def threesum(nums):
    n= len(nums)
    my_set = set()

    for i in range(n):
        for j in range(i+1,n):
            for k in range (j+i,n):
                if nums[i]+nums[j]+nums[k]==0:
                    temp =[nums[i]+nums[j]+nums[k]]
                    my_set.add(tuple(temp.sort()))
    return [list(ans) for ans in my_set]




def three_sum(nums:list):
     aftersort = nums.sort()
     result =[]

     for i in  range(len(nums)):

          if i>0 and nums[i]==nums[i-1]:
              continue

          left=i+1
          right =len(nums)-1

          while left<right:

              total = nums[i] + nums[left] + nums[right]

              if total ==0:
                  result.append([
                      nums[i] ,nums[left] , nums[right]
                  ])

                  left+=1
                  right-=1


                  while left<right and nums[left]==nums[left-1]:
                     left+=1


                  while left<right and nums[right]==nums[right+1]:
                     right-=1

              elif total <0:
                  left+=1

              else:
                  right -=1


     return result
                  
   

                            


