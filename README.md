# Countdown Application

## Project Overview
The Countdown Application is a Python-based tool that allows users to set a goal and a deadline, then calculates and displays the time remaining until the specified deadline. This simple yet effective utility helps users track their objectives and stay motivated.

## Features
- **User Input:** Accepts a goal and a deadline in the format `goal:dd.mm.yyyy`.
- **Validation:** Ensures the input format is correct and validates the deadline date.
- **Time Calculation:** Computes the remaining days and hours until the deadline.
- **Feedback:** Notifies the user if the deadline has already passed.

## Technologies Used
- **Python:** Core language for implementing the application logic.
- **IntelliJ IDEA:** IDE for development and testing.
- **Git:** Version control for code management.

## File Structure
```
countdown-app/
├── time-till-deadline.py
├── helper.py
└── README.md
```

### File Descriptions
- `time-till-deadline.py`: Main script for handling user input, validating it, and calculating the time remaining until the deadline.
- `helper.py`: Contains utility functions such as `validate_date` for verifying date formats.

## How to Run the Application

### Prerequisites
1. **Python 3.x:** Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).
2. **IntelliJ IDEA (optional):** Recommended for editing and running the code.
3. **Git (optional):** Clone the repository using Git for version control.

### Steps to Run
1. Clone the repository (if applicable):
   ```bash
   git clone <repository_url>
   cd countdown-app
   ```
2. Run the main script:
   ```bash
   python3 time-till-deadline.py
   ```
3. Follow the prompts to enter your goal and deadline in the specified format, e.g., `Learn Python:25.12.2024`.

### Example
**Input:**
```
Enter your goal with a deadline separated by a colon (e.g., Learn Python:25.12.2024)
Learn Python:25.12.2024
```

**Output:**
```
Valid date: 25.12.2024
Dear user! Time remaining for your goal: 'Learn Python' is 8760 hours.
```

## Error Handling
- Invalid input format:
  ```
  Invalid input format. Please use 'goal:dd.mm.yyyy'.
  ```
- Invalid date format:
  ```
  Invalid date format. Please use 'dd.mm.yyyy'.
  ```
- Passed deadlines:
  ```
  Deadline for your goal: Learn Python has already passed.
  ```



---

Start setting your goals today with the Countdown Application and make every moment count!
