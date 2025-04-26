def reverse(s):
  string=""
  #loop through the string in reverse order
  for char in s:
    #add each character to the string
    string=char+string
  return string

#test the function
print(reverse("hello world"))	