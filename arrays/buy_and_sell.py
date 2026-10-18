
def  buy_and_sell(nums:list):
    buy=0
    sell=0

    max_profit =0
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if nums[j]>nums[i]:
                profit = nums[j]-nums[i]
                max_profit = max(max_profit,profit)

    return max_profit



nums =[1,4,3,5,10]
print(buy_and_sell(nums=nums))


def  buy_and_sell(nums:list):

    max_profit =0
    min_price =float("inf")
    n=len(nums)
    for i in range(n):
        min_price = min(min_price,nums[i])
        max_profit = max(max_profit,nums[i]-min_price)
    return max_profit,min_price,nums[i]

print(buy_and_sell(nums))
