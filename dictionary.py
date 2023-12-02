ages = {"Adejoke": 9, "Nola": 9, "Dara": 11, "Teacher": 20}
print("Dictionary of ages:", ages)

#Example 1: Dictionary of ages:
ages = {"Alice": 10, "Bob": 12, "Charlie": 11, "David": 9, "Eva": 13}
print("Dictionary of ages", ages)

#Example 2:Dictionary of book titles and their authors
books = {"Python Crash Course": "Eric Matthes", "Deep Learning": "Ian Goodfellow"}
print("Dictionary of books", books)

# Example 3: Dictionary of superhero powers
superheroes = {"Superman": "Flying", "Batman": "Gadgets", "Wonder Woman": "Lasso of Truth"}
print("Dictionary of superheroes:", superheroes)

#Example 4: Accessing elements in a dictionary
alice_age = ages["Alice"] # Accessing Alice's age: 10
print("Alice's age:", alice_age)

book_author = books["Python Crash Course"] # Accessing the author of the book "Python Crash Course"
print("Author of Python Crash Course:", book_author)

#Example 5: Modifying dictionaries
ages["Eva"] = 14 # Updating Eva's age to 14
print("Updating ages:", ages)

books["Deep Learning"] = "Yoshua Bengio" # Correcting the author of the book "Deep Learning"
print("Updated books:", books)

superheroes["Batman"] = "Utility Belt" # Updating Batman's power
print("Updated superheroes:", superheroes)