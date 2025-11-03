def approve_loan(name, income, credit_score):
    if income > 40000 and credit_score > 700:
        return f"Loan approved for {name}"
    else:
        return f"Loan rejected for {name}"

print(approve_loan("John", 50000, 720))
print(approve_loan("Mary", 50000, 720))
