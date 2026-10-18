numbers =[1,2,3,4]
numbers.append(5)
print(numbers)
numbers.append([4,5])
print(numbers)
numbers.extend(numbers)
numbers2 = numbers

print(numbers2 == numbers
)


#insert

numbers.insert(2,30)
print(numbers)


numbers.remove(30)
print(numbers)

numbers.pop()
print(numbers)

del numbers[1]
print(numbers)

find:list= list(reversed(numbers))

