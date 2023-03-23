import datetime
datetime1 = datetime.datetime.now()
if (datetime1.hour < 6):
    print("Good Night Sir")
elif (datetime1.hour > 6 and datetime1.hour < 12):
    print("Good Morning sir")
elif (datetime1.hour > 12 and datetime1.hour < 18):
    print("Good Afternoon Sir")
elif (datetime1.hour > 18 and datetime1.hour < 20):
    print("Good Evening Sir")
elif (datetime1.hour > 20):
    print("Good Night Sir")
