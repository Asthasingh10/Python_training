# ### **1. Employee Attendance Tracker**
# - Implement a system that tracks employee attendance.
# - Use loops to process multiple employees and conditionals to check attendance.
# - Mark employees as "Needs Attention" if absent for more than 3 consecutive days.

def employee_attendance_tracker():
    num_employees = int(input("Enter the number of employees: "))
    days = int(input("Enter number of days to track: "))
    attendance_data = {}
    for _ in range(num_employees):
        name = input("\nEnter employee name: ")
        print(f"Enter attendance for {name} (P for Present, A for Absent):")
        records = []
        for day in range(1, days + 1):
            status = input(f" Day {day}: ").upper()
            records.append(status)
        attendance_data[name] = records
    print("\n--- Attendance Report ---")
    for name, records in attendance_data.items():
        consecutive_absent = 0
        needs_attention = False
        for status in records:
            if status == 'A':
                consecutive_absent += 1
                if consecutive_absent > 3:
                    needs_attention = True
                    break
            else:
                consecutive_absent = 0
        status_note = "Needs Attention" if needs_attention else "OK"
        print(f"{name}: {''.join(records)} -> {status_note}")
employee_attendance_tracker()
