numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

quantity_ = len(numbers)

index_ = numbers.index(None)
numbers[index_] = 0
sum_1 = sum(numbers[0:index_])
sum_2 = sum(numbers[index_:])
sum_ = sum_1 + sum_2

average_ = sum_ / (quantity_)

numbers[index_] = average_
print("Измененный список:", numbers)
