weight = int(input('Weight: '))
unit = input('L(lbs) K(g)')
if unit.upper() == 'L':
  print(weight * 0.45)
elif unit.upper() == 'K':
  print(weight / 0.45)
else:
  pass