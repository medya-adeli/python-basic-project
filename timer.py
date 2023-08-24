import time

def timer():
    second = 0
    minute = 0
    hours = 0
    day = 0
    
    second_1 = int(input("Enter seconds: "))
    minute_2 = int(input("Enter minutes: "))
    hours_3 = int(input("Enter hours: "))
    day_4 = int(input("Enter days: "))
    
    x = 1
    while day < day_4 or hours < hours_3 or minute < minute_2 or second < second_1:
        time.sleep(x)
        second += 1
        if second == 60:
            second = 0
            minute += 1
        if minute == 60:
            minute = 0
            hours += 1
        if hours == 24:
            hours = 0
            day += 1
        print("--------------------------------------------------------")
        print(f"Day:{day:02d}|Hours:{hours:02d}|Minute:{minute:02d}|Second:{second:02d}")

timer()
