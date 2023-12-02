toys = ["dolls", "cars", "blocks"]
print(toys)

first_toy = toys[0]
print(first_toy)

last_toy = toys[-1]
print(last_toy)

# Example 1: List of fruits
fruits = ["apple", "banana", "orange", "grape", "watermelon"]
print("List of fruits:", fruits)

# Example 2: List of numbers
numbers =[1, 2, 3, 4, 5]
print("List of numbers:", numbers)

# Example 3: List of mixed types
mixed_list = ["apple", 2, True, 4.5, "banana"]
print("Mixed list:", mixed_list)

#Example 4: Accessing elements in a list
first_fruit = fruits[0]  # Accessing the first fruit: "apple"
print("First fruit:", first_fruit)

second_number = numbers[1] # Accessing the second number: 2
print("Second number:", second_number)

#Example 5: Modifying lists
fruits.append("pear") # Adding "pear" to the fruits list
print("Updated list of fruits:", fruits)

numbers.insert(5, 6) # Inserting number 6 at index 5 in numbers
print("Updated list of numbers:", numbers)
mixed_list.remove(True) # Removing the true value from mixed_list
print("Updated mixed list:", mixed_list)