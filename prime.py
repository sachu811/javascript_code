
def prime(num):
  print(num%23)
  for i in range(2,int(num**0.5)+1):
    if num%i==0:
      return i
  return "Yes prime number"
print(prime(1627))



