from datetime import datetime
def validate_date(date_str):
    try:
        # Attempt to parse the date
        valid_date = datetime.strptime(date_str, "%d.%m.%Y")
        print(f"Valid date: {valid_date.strftime('%d.%m.%Y')}")
        return True
    except ValueError:
        # Handle invalid date format
        print("Invalid date format. Please enter the date in DD.MM.YYYY format.")
        return False