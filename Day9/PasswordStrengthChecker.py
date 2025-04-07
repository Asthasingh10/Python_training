# Classify passwords as "Weak", "Medium", or "Strong" based on length, numbers, uppercase/lowercase letters, and special characters.
# - Loop until a "Strong" password is entered.
import re

def classify_password(password):
    length = len(password) >= 8
    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    has_digit = bool(re.search(r"[0-9]", password))
    has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    score = sum([length, has_upper, has_lower, has_digit, has_special])
    print(score)
    if score <= 2:
        return "Weak"
    elif score == 3 or score == 4:
        return "Medium"
    else:
        return "Strong"
# Loop until strong password is entered
while True:
    user_password = input("Enter your password: ")
    strength = classify_password(user_password)
    print(f"Password Strength: {strength}")

    if strength == "Strong":
        print("✅ Password accepted!")
        break
    else:
        print("❌ Try again with a stronger password.\n")
