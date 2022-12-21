numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)  # [1, 2, 3, 4, 5, 6]
numbers.insert(0, -1)
print(numbers)  # [-1, 1, 2, 3, 4, 5, 6]
numbers.remove(1)
print(numbers)  # [-1, 2, 4, 5, 6]
# numbers.clear() # []
print(1 in numbers) # True
print(10 in numbers) #False
print(len(numbers)) #6
