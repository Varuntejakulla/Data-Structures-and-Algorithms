def spiral_matrix(nums):
    cols = len(nums[0])
    top = 0
    left=0
    bottom = cols-1
    right  = cols-1

    for i in range(left,right):
        print(nums[top][i])
    top+=1
    for i in range(top,bottom):
        print(nums[i][right])
    right-=1

    for i in range(right,left):
        print(nums[bottom][i])
    bottom-=1

    for i in range(bottom,top):
        print(nums[i][left])
    left+=1



nums =[[1,2,3,4],[5,6,7,8],[9,10,11,12],[[13,14,15,16]]]

spiral_matrix(nums=nums)