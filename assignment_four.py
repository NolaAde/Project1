username = "user123"
password = "secret123"
if username == "admin" and password == "admin123":
    print("Admin access granted")
elif username == "user123" and password == "secret123":
    print("User access granted")
else:
    print("Access denied")