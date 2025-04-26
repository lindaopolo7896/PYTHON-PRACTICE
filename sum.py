#Function to find the sum of a list of numbers
def mysum(numbers):
  sum=0
  for number in numbers:
    sum+=number
  return sum

myList = [10,12,23,17,19,67]
print("Sum =", mysum(myList))