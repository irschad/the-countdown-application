from datetime import datetime
from helper import validate_date

user_input = input("Enter your goal with a deadline separated by a colon (e.g., Learn Python:25.12.2024)\n")
input_list = user_input.split(":")

# Validate the input
if len(input_list) != 2:
    print("Invalid input format. Please use 'goal:dd.mm.yyyy'.")
    exit()

goal = input_list[0].strip()
deadline = input_list[1].strip()

# Validate date in input
if not validate_date(deadline):
    print("Invalid date format. Please use 'dd.mm.yyyy'.")
    exit()

# Calculate the deadline date
deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.today()

# Calculate how many days and hours are remaining
time_till = deadline_date - today_date
if time_till.days < 0:
    print(f"Deadline for your goal: {goal} has already passed.")
else:
    hours_till = int(time_till.total_seconds() / 60 / 60)
    print(f"Dear user! Time remaining for your goal: '{goal}' is {hours_till} hours.")
