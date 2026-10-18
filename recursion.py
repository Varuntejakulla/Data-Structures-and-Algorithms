
#recursion understanding 

def function(count):
    if count==4:
        return 
    print("varun")

    return function(count+1)



function(0)


def sumofnumbers(start,ending,sum):
    if start>ending:
        print(sum)
        return 
    return sumofnumbers(start+1,ending,sum+start)

sart,ending,sum =1,50,0

sumofnumbers(sart,ending,sum)



def facrtorail(number):
    if number==1:
        return 1
    return number*facrtorail(number-1)

print(facrtorail(5))

