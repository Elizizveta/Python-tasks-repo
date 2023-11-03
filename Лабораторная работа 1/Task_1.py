numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
index = numbers.index(None)
numbers.remove(None)
average = sum(numbers)/(len(numbers)+1)
numbers = numbers[0:index]+[average]+numbers[index:]
print("Измененный список:", numbers)
