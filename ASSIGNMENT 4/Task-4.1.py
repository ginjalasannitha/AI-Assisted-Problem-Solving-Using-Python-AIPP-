# Function to check if a year is a leap year
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


# Loop for multiple inputs
while True:
    year = int(input("Enter a year: "))
    
    if is_leap_year(year):
        print(year, "is a leap year.")
    else:
        print(year, "is not a leap year.")
    
    choice = input("Do you want to check another year? (yes/no): ").lower()
    if choice != "yes":
        print("Exiting program. Goodbye!")
        break
