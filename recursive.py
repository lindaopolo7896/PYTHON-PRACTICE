#Function to get the factorial of a number using recursion
def recursive_function(x):
  #base case
  if x == 0 or x == 1:
    return 1
  #recursive case
  else:
    return x * recursive_function(x - 1)
  
# Test the recursive function
print(recursive_function(5))