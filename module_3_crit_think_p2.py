while True:
    try:
        # Get the current time from user
        current_time = int(input("Enter the current time in hours (0 to 23): "))
        if 0 <= current_time <= 23:
            break
        else:
            print("Invalid input. Please enter a number between 0 and 23.")
    except ValueError:   # If user entered something that couldn't be converted to an integer
        print("Invalid input. Please enter a whole number.")
        
while True:
    try:
        # Get the number of hours to wait for the alarm
        hours_to_wait = int(input("Enter the number of hours to wait for the alarm: "))
        if hours_to_wait >= 0:
            break
        else:
            print("Invalid input. Please enter a non-negative number.")
    except ValueError:   # If user entered something that couldn't be converted to an integer
        print("Invalid input. Please enter a whole number.")
        
# Calculate the alarm time
alarm_time = (current_time + hours_to_wait) % 24

print("The alarm will go off at", alarm_time, "hours on a 24-hour clock.")