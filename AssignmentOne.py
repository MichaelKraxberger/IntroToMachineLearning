"""
Michael Kraxberger
1/25/2023
Introduction to Machine Learning
Assignment One
"""

import math

# Question One
print("----Question One----\n")
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()  # Sorted Ages
ages.insert(0, min(ages))  # Inserting the min value at index 0 to keep the sort
ages.append(max(ages))  # Appended the max value to ages to keep the sort
ages_median = ages[len(ages) // 2] if len(ages) % 2 == 0 else (ages[len(ages) // 2] + ages[
    math.ceil(len(ages) / 2)]) / 2  # Ternary to determine whether it is a value or the average of 2 values
ages_average = sum(ages) / len(ages)
ages_range = max(ages) - min(ages)
print(f"Sorted, with inserted values: {ages}\nMedian: {ages_median}\nMean (Average): "
      f"{ages_average}\nRange: {ages_range}\n\n")

# Question Two
print("----Question Two----\n")
print("--Dog--")
dog = {}  # Create empty dog Dict
dog['name'], dog['color'], dog['breed'], dog['legs'], dog['age'] = ' ', ' ', ' ', ' ', ' '  # Fill the Dict
print(f"Dog: {dog}\n")

print("--Student--")
student = {'first_name': None, 'last_name': None, 'gender': None, 'age': None, 'marital_status': None, 'skills': [],
           'country': None, 'city': None, 'address': None}  # Create and assign keys to student Dict
print(f"Students Length: {len(student)}\nSkills Value: {student['skills']}\nSkills Type: {type(student['skills'])}")

student['skills'] = ["Python", "Java"]  # Assign Values to skills
print(f"Keys: {list(student.keys())}")
print(f"Values: {list(student.values())}\n\n")

# Question Three
print("----Question Three----\n")
brothers = ("Clay", "Trey", "Landon")  # Creating brothers
sisters = ("Makenzie", "Emily", "Bree")  # Creating sisters
siblings = brothers + sisters  # Concatenating brothers and sisters into siblings
print(f"Siblings: {siblings}")
print(f"Number of Siblings: {len(siblings)}")
family_members = siblings + ("Jim", "Michelle")  # Adding parents into siblings / family members
print(f"Family Members: {family_members}\n\n")

# Question Four
print("----Question Four----\n")
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(f"Length of Set it_companies: {len(it_companies)}")
it_companies.add("Twitter")  # Adding Twitter
it_companies.update(["Samsung", "Cisco", "Meta"])  # Adding Samsung, Cisco, and Meta
print(f"it_companies (before remove): {it_companies}")
it_companies.remove("Facebook")  # Removing Facebook
print(f"it_companies (after remove): {it_companies}")
C = A.union(B)  # Joining A and B into C to preserve A
print(f"Set C (A join B): {C}")
print(f"A intersection B: {A.intersection(B)}")
print(f"Is A a Subset of B: {'YES' if A.issubset(B) else 'NO'}")
print(f"Are A and B disjoint sets: {'YES' if A.isdisjoint(B) else 'NO'}")
A.update(B)  # Join A to B
B.update(A)  # Join B to A
print(f"Symmetric Differences of A and B: {A.difference(B)}")
A.clear()  # Clearing A
B.clear()  # Clearing B
print(f"Cleared Sets: {A}, {B}")
print(f"Length of Ages List: {len(age)}\nLength of Ages Set: {len(set(age))}\n\n")

# Question Five
print("----Question Five----\n")
rad = 30
_area_of_circle_ = math.pi * rad ** 2  # calculate area
_circum_of_circle = math.pi * 2 * rad  # calculate circumference
print(f"Area: {_area_of_circle_}\nCircumference: {_circum_of_circle}")
radius = eval(input("Enter a radius: "))  # enter a radius and evaluate the type (make it an int)
print(f"Area of Circle with Radius {radius}: {math.pi * radius ** 2}\n\n")


# Question Six
print("----Question Six----\n")
teacher_str = "I am a teacher and I love to inspire and teach people"
A = set(str.split(teacher_str))  # split the string by spaces into a set
print(f"Unique words in the string: {len(A)}\n\n")

# Question Seven
print("----Question Seven----\n")
print(f"Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki\n\n")

# Question Eight
print("----Question Eight----\n")
radius = 10
area = 3.14 * radius ** 2
print(f"The area of  circle with radius {radius} is {area:.0f} meters square.\n\n")

# Question Nine
print("----Question Nine----\n")
lbs = str.split(input("Enter weights separated by spaces (ex. 10 20): "))
lbs = list(map(int, lbs))  # set pounds to an integer array
kg = [round(i / 2.205, 2) for i in lbs]  # loop through pounds, set it to KGs rounded
print(f"Pounds: {lbs}")
print(f"Kilograms: {kg}")
