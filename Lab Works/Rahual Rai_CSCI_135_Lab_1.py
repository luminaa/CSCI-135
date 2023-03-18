"""
Q1) Write a program that stores your name in a variable and then print the variable 
"""
# stores my name in a variable called 'name'
name = "Rahual Rai" 
# prints my name
print(name) 



"""
Q2) L = ["Spring", "Summer", "Fall", "Winter", 1, 2, 3]
Given the list above, using a for loop, write a program to print out the values in the list, sequentially. Your output should look like this:
Spring
Summer
Fall
Winter
1
2
3
"""
# stores the elements in a list
L = ["Spring", "Summer", "Fall", "Winter", 1, 2, 3] 
# iterates through the list 'L' and assigns each element the variable name 'outp'
for outp in L: 
	# prints the element that is assign was outp in each iteration
	print(outp) 



"""
Q3) X = 6
Given X above, write a program using an if statement to display if the number stored in X is an even or odd number.
"""
# assigns integer 6 to variable called 'X'
X = 6 
# % is a modulo operation and if the number is divisible by 2 and does not give any remainder, the number must be even.
if X%2 == 0: 
	# if the number is even
	print('number is even')
else: 
	# if the number is not even, it must be odd.
	print('number is odd')



"""
Q4) Using a while loop, write a program to calculate the sum of the numbers from 1 to 50. Your program should print the result of this calculation
"""
# initializes the variables, x is the number and ans is the sum of the numbers
x, ans = 1, 0 
# loops as long as x is less than or equals to 50
while x<=50: 
	# increment the ans counter by the number it is on, x
	ans += x 
	# increment the ans counter by 1
	x += 1 
# print ans
print(ans)