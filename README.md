# Assignment_5_for_practice

# Assignment 5: Module 6 - Data Structures and Strings in Python

## Overview
This assignment covers the basics of Python **dictionaries**, **list slicing**, and **string manipulations**.  
It demonstrates:
1. Looking up values in a dictionary using user input.
2. Extracting and reversing elements from a list using slicing.

---

## Task 1: Create a Dictionary of Student Marks

**Description:**  
- A dictionary stores student names as keys and their marks as values.
- The user is prompted to enter a student's name.
- The program checks if the name exists in the dictionary and displays the marks.
- If the name is not found, a "Student not found" message is displayed.

**Code Snippet:**
```python
students = {"Himanshu": 70, "Hemant": 89, "Taksh": 90, "Payal": 95}
name = input("Enter the student's name: ")

if name in students:
    print(f"{name}'s marks: ", students[name])
else:
    print("Student not found.")

Example Output:
Enter the student's name: Taksh
Taksh's marks: 90


Task 2: Demonstrate List Slicing
Description:
Creates a list of integers from 1 to 10.
Extracts the first five elements using slicing.
Reverses the extracted elements using slicing with a negative step.

Code Snippet:

list1 = [1,2,3,4,5,6,7,8,9,10]
print("Original List: ", list1)
print("Extracted first five elements: ", list1[0:5])
print("Reversed extracted element: ", list1[0:5][::-1])

Example Output:
Original List:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Extracted first five elements:  [1, 2, 3, 4, 5]
Reversed extracted element:  [5, 4, 3, 2, 1]


