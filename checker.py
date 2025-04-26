#Function to check if a number is even or odd
def checker():
  number=int(input("Enter a number: ")) # Get user input
  # Check if the number is even or odd
  if number % 2 == 0:
    print("Even")
  else:
    print("Odd")

checker()