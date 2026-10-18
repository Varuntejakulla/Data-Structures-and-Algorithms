import math

#counting numbers 
def counting(num):
    count =0
    while num>0:
        count+=1
        num//=10
    return count

#counting numbers using ther  logrithm 

def  countingusinglog(num):

    return round(math.log10(num))

def reverse_number(num):
    rev =0 
    while num>0:
        last =num%10  #if want last number
        rev = rev*10+last
        num //=10 #if want remove the last number 
    return rev


def amstrong_number(num):
    original =num
    count= int(math.log10(num)+1)
    amstrong =0

    while num >0:
        last_digit = num%10
        amstrong+= last_digit**count
        num//=10
    return amstrong==original





print(counting(3216))

print(countingusinglog(3216))

print(reverse_number(321))

print(amstrong_number(153))