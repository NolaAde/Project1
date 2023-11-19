import datetime
hour = datetime.datetime.now().hour
if hour < 12:
    print("Good Morning")
elif hour < 17:
    print("Good Afternoon")
else:
    print("Good Evening")