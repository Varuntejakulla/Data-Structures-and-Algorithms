class Binary_search:
    def __init__(self,nums:list,target:int):
        self.nums = sorted(nums)
        self.target = target
        self.n = len(nums)


    def binary_search(self):
        low = 0
        high = self.n-1
        

        while low<=high:
            mid = low +high //2
            if self.nums[mid] == self.target:
                return mid

            elif self.nums[mid]<self.target:
                low= mid+1
            else:
                high =mid-1

        return -1



nums =[3,1,2,100,6,3,5,2,5,2]

search = Binary_search(nums=nums,target=100)
print(search.binary_search()
)


             

    