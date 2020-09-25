secret = 16 
count = 0
limit = 3
while count < limit:
  guess = int(input('Guess: '))
  count += 1
  if guess == secret:
    print('You Won!!')
    break
else:
  print('Sorry, You failed!')
  