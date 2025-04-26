# Function to calculate the sum of digits of a given number
def sum_digits(n):
  total = 0
  while n > 0:
    total += n % 10 # Add the last digit to total
    n //= 10 # Remove the last digit from n
  return total

# Test the function
print(sum_digits(12345)) 