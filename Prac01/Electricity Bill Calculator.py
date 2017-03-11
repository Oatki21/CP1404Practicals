tariff_value = 0
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
tariff_input = int(input("Which tariff? 11 or 31:"))
if tariff_input == 11:
    tariff_value = TARIFF_11
elif tariff_input == 31:
    tariff_value = TARIFF_31
else:
    print("Error, Please enter an acceptable value.")
    tariff_input = int(input("Which tariff? 11 or 31:"))
dailyUse = float(input("Enter daily use in kWh:"))
billDays = int(input("Enter the number of billing days:"))
estimatedBill = tariff_value * dailyUse * billDays
print("Estimated bill:$", estimatedBill)

