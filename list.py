numbers = [97, 63, 66, 72, 82, 92, 78, 55]
high = numbers[0]
for number in numbers:
  if number > high:
    high = number
print(high)