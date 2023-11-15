age = input("What is your current age?\n")

age_limit = 90
age_left = age_limit - int(age)

age_left_days = 365 * age_left
age_left_weeks = 52 * age_left
age_left_months = 12 * age_left

print(
    f"You have {age_left_days} days, {age_left_weeks} weeks, and {age_left_months} months left."
)
