def factorial(val):
  fact=1
  while val !=1:
    fact*=val
    val-=1
  return fact

print(factorial(4))