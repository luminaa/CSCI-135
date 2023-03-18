"""
1. Write a program that performs the following tasks:
 
a) Ask the user to insert 5 strings into a list named temp
    (i) Split  temp and store it in a variable named student i.e. student = temp.split()

b)    Create a second list named midterm of the same size as students; fill in the list, midterm with integers in the range 0 to 100.

c)  Print out the members of the two list such that each line has a member of students and grades    
 
Below is sample output that your program should resemble:

Enter 5 student names:
Adam Levine
Beyonce
Calvin Harris
DJ Snake
Eminem

Here are the midterm grades of the 5 students above:
Adam Levine :  20
Beyonce : 50
Calvin Harris : 70
DJ Snake : 100
Eminem : 5
"""

# part (a)

print("Enter 5 student names:")

# Initializing an empty list to store the student names
student_name_list = [] 

# Looping to input 5 student names and store them in a variable named student
while len(student_name_list)<5: 
    temp = input().strip()
    student_name_list.append(temp)

# part (b)

# Prompting the user to enter the grades of the 5 students respectively
midterm = input("Enter grades of students in respective order in first input: ")

# splitting the grades and storing them in a list 
midterm = midterm.split() 

# part (c)

# Looping through the student name list and their respective grades
for name, grade in zip(student_name_list, midterm): 

    # printing the student name and their grade
    print(f"{name} : {grade}") 


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


"""
2. my_dict = {'a':100,'b':-54,'c':247,'d':200 ,'e':150 ,'f':25 ,'g':16}

Given the dictionary, my_dict above, write a Python program to sum all the items in a dictionary.
"""

my_dict = {'a':100,'b':-54,'c':247,'d':200 ,'e':150 ,'f':25 ,'g':16}

# Initialize a variable to store the sum of items in the dictionary
total_sum = 0

# Iterate through the items in the dictionary
for value in my_dict.values():
  # Add each value to the variable
  total_sum += value

# Print the total sum of all the items in the dictionary
print(total_sum)