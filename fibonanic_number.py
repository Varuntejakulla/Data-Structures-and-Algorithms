
def recursion_of_the_fibinioanic(number):

      if number ==0 :
            return 0
      if number ==1 or number ==2:
            return 1

      return recursion_of_the_fibinioanic(number-1)+recursion_of_the_fibinioanic(number-2)


print(recursion_of_the_fibinioanic(9))