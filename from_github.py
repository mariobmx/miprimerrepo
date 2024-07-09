def myfactorial(x):
  cont = 1
  prod = 1

  while cont <= x:

    prod = prod*cont

    cont = cont + 1

  return prod

print('El factorial de ', x, 'es ', myfactorial(x))

