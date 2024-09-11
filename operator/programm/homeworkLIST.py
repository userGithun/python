                                                         #program1


# # Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Create a new list with each number squared
squared_numbers = [x**2 for x in numbers]

# Print the original and new lists
print("Original numbers:", numbers)
print("Squared numbers:", squared_numbers)


                                                         #program 2

# Create two lists
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

# Slice the first list to get the first three elements
slice_list1 = list1[:3]

# combining the two lists
combined_list = list1 + list2

# Print the results
print("Sliced list1:", slice_list1)
print("Combined list:", combined_list)


                                                         #program3

a =['apple','banana','cherry']
a[1],a[2]=a[2],a[1] 
print(a)

                                                         #program4

# Create a list with numbers
numbers = [1, 2, 3, 4, 5]

# Access and print the first and last elements
print("First number:", numbers[0])
print("Last number:", numbers[-1])

                                                          #program5

# Create a list with some fruits
fruits = ["apple", "banana", "cherry"]

# Add a new fruit and remove an existing one
fruits.remove("banana")
fruits.append("date")

# Print the updated list
print("Updated fruits list:", fruits)