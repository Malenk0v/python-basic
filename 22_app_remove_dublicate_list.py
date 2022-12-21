numbers = [2, 2, 4, 6, 3, 4, 6, 1]
result = []

for number in numbers:
    if number not in result:
        result.append(number)
    # while numbers.count(number) > 1:
    #     numbers.remove(number)
print(result)
