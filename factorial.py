#Funtion to calculate the factorial of a number
def factorial(n):
  r=1
  # Loop to calculate factorial
  for i in range(1,n+1):
    r*=i
  return r

print(factorial(5))