def factorial(num):
  """calculates factorial of a number using recursion"""
  if num == 0 or num == 1: # base cases
    return 1
  return num * factorial(num-1) # recursion with num-1
        
def sums(num):
  """calculates the sum of numbers from 0 to 'num' using recursion"""
  if num == 0: # base case
    return 0
  if num == 1: # base case
    return 1
  return num + sums(num-1) # recursion with num-1

# open file 'recursion.txt' and iterate over each line
with open('recursion.txt') as file:
  for line in file:
    n = int(line.strip()) # strip whitespace from line and convert it to integer
    if n < 0: # check if n is negative
      print("number is negative")
      continue # skip to next iteration
    factorial_n = factorial(n)
    sum_n = sums(n)
    print(f"factorial sum: {factorial_n} {sum_n}")