
# Problem 6: Bank Loan Eligibility System**
# Bank Loan Eligibility System
salary = int(input("Enter your monthly salary (in ₹): "))
age = int(input("Enter your age: "))
credit_score = int(input("Enter your credit score: "))

# Check eligibility using nested conditionals
if salary >= 25000:
    if 21 <= age <= 60:
        if credit_score >= 700:
            print("✅ You are eligible for a bank loan!")
        else:
            print("❌ Sorry, your credit score is too low.")
    else:
        print("❌ Sorry, your age does not meet the requirement.")
else:
    print("❌ Sorry, your salary is too low for loan eligibility.")
