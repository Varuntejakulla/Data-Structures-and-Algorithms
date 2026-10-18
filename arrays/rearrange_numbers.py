def rearrange_numbers(nums:list):
     pos = []
     neg =[]

     for num in nums:
          if num>=0:
               pos.append(num)
          else:
              neg.append(num)

     for i in range(0,len(pos)):
          nums[2*i]=pos[i]
          nums[(2*i)+1]=neg[i]

     return nums

nums=[1, 3, -1,2, -2,  -3, ]

print(rearrange_numbers(nums=nums))



      