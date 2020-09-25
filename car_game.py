command = ''
started = False
while True:
  command = input('> ').lower()
  if command == 'start':
    if started:
      print('Program already started')
    else:
      started = True
      print('Car started...')
  elif command == 'stop':
    if not started:
      print('Program already stopped')
    else:
      started = False
      print('Car stopped...')
  elif command == 'help':
    print('''
- Start to start the car
- Stop to stop the car
- Quit to quit..
    ''')
  elif command == 'quit':
    break
  else:
    print('Sorry, command not found...')
