'''
ASSIGNMENT 5:
Module 6: Data Structures and Strings in Python

Task 1: Create a Dictionary of Student Marks
'''

students = {"Himanshu": 70, "Hemant": 89, "Taksh": 90, "Payal": 95}
name = input("Enter the student's name: ")

if name in students:
    print(f"{name}'s marks: ", students[name])
else:
    print("Student not found.")



# Task 2: Demonstrate List Slicing
list1 = [1,2,3,4,5,6,7,8,9,10]
print("Original List: ", list1)
print("Extracted first five elements: ", list1[0:5])
print("Reversed extracted element: ", list1[0:5][::-1])

