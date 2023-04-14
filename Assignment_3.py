import numpy
import matplotlib.pyplot as plot

print(f"{'_'*20}Question 1a{'_'*20}")
# Making random vector
print("\nMaking Vector")
vect = numpy.random.randint(1, 20, 15)
print(vect)

# Reshape vector to 3x5
print("\nReshaping Vector")
vect = vect.reshape(3, 5)
print(vect)

# Replace max in vect rows with 0
print("\nReplacing Max Values")
for row in vect:
	row[row == row.max()] = 0
print(vect)

# Create 2d array 4x3, then print the shape, type, and data
print("\nCreating 2d array sized 4x3, then printing the shape, type, and data")
vect = numpy.random.randint(1, 20, (4, 3))
print(f"Array:\n{vect}\nShape: {vect.shape} Type: {type(vect)} Data Type: {vect.dtype}")

print(f"\n{'_'*20}Question 1b{'_'*20}")
# Make and print array
print("Making Array")
arr = numpy.array([[3, -2],[1, 0]])
print(arr)

# Creating Eigen Value and Vector Vars and assigning vals
print("\nCreating Eigen Value and Vector Vars and assigning vals")
eign_val, eign_vect = numpy.linalg.eig(arr)
print(f"Eigen Value: {eign_val}\nEigen Vector:\n{eign_vect}")

print(f"\n{'_'*20}Question 1c{'_'*20}")
# Creating array
print("Creating Array:")
arr = numpy.array([[0, 1, 2],[3, 4, 5]])
print(arr)

# Computing Values and printing
print("\nComputing Diagonal Values: ")
diag = arr.trace()
print(diag)

print(f"\n{'_'*20}Question 1d{'_'*20}")
# creating array
print(f"Creating Array: ")
arr = numpy.array([[1, 2], [3, 4], [5, 6]])
print(arr)

# reshaping
arr = arr.reshape(2, 3)
print(f"\nReshaped to 2x3:\n{arr}")

arr = arr.reshape(3, 2)
print(f"\nReshaped to 3x2:\n{arr}")

print(f"\n{'_'*20}Question 2{'_'*20}")

# Sample Data
programming_languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = numpy.array([22.2, 17.6, 8.8, 8, 7.7, 6.7])

# Creating Chart with popularity mapped
print("Creating Chart. . .")
chart = plot.pie(popularity, labels=programming_languages, shadow=True, autopct='%1.1f%%')

# Printing
plot.show()
