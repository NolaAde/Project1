print("You are in a magical land with three doors")
door = input("Which door will you choose(1, 2, 3)?")
if door == "1":
    print("You found a hidden treasure! Congratulations!")
elif door == "2":
    print("A friendly dragon appears and offers you a wish. What do you wish for?")
    wish = input("I wish for:")
    print(f"You wished for {wish}. The dragon grants your wish!")
elif door == "3":
    print("Oops! You fell into a pit, but a helpful squirrel rescues you.")
else:
    print("Invalid choice. Please choose a door(1, 2, or 3).")