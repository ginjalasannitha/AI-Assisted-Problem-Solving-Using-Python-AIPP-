# bill.py
# Electricity Bill Generator for TGNPDCL
# Assignment Number 03.3
# Read inputs
PU = int(input("Enter previous reading (PU): "))
CU = int(input("Enter current reading (CU): "))
customer_type = input("Enter customer type (Domestic/Commercial/Industrial): ")
# Calculate units consumed
units = CU - PU
# Initialize charges
EC = FC = CC = ED = LOSS_GAIN = 0
# Calculate based on customer type
if customer_type.lower() == "domestic":
    if units <= 100:
        EC = 237.80        # From actual bill
        FC = 20.00          # Fixed charge
        CC = 70.00          # Customer charge
        ED = 5.76           # Electricity duty
        LOSS_GAIN = 0.44    # Loss/gain adjustment
    else:
        # For higher units, you can extend slab logic
        EC = (100 * 2.478) + ((units - 100) * 3.00)
        FC = 30.00
        CC = 10.00
        ED = 0.058 * EC
elif customer_type.lower() == "commercial":
    EC = units * 5.00
    FC = 50.00
    CC = 15.00
    ED = 0.058 * EC
elif customer_type.lower() == "industrial":
    EC = units * 6.00
    FC = 75.00
    CC = 20.00
    ED = 0.058 * EC
else:
    print("Invalid customer type entered.")
    exit()
# Total Bill
bill = EC + FC + CC + ED + LOSS_GAIN
# Print Bill
print("\nTGNPDCL ELECTRICITY BILL")
print("------------------------")
print(f"Customer Type : {customer_type.capitalize()}")
print(f"Previous Units: {PU}")
print(f"Current Units : {CU}")
print(f"Units Consumed: {units}\n")
print(f"Energy Charges (EC): ₹{EC:.2f}")
print(f"Fixed Charges  (FC): ₹{FC:.2f}")
print(f"Customer Charges(CC): ₹{CC:.2f}")
print(f"Electricity Duty (ED): ₹{ED:.2f}")
print(f"Loss/Gain Adj. (LG): ₹{LOSS_GAIN:.2f}")
print("--------------------------------")
print(f"Total Bill Amount : ₹{bill:.2f}")