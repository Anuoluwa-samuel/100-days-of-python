print("Welcoome to the tip calculator")
Bill = float(input("what was the  bill? \n"))
tip = int(input("What percentage of tip would you love to give?, 10, 12 or 15 \n"))
if tip == 10:
    print("Your tip is 10%")
    print("Your total bill is $" + str(Bill * 1.1))
elif tip == 12:
    print("Your tip is 15%")
    print("Your total bill is $" + str(Bill * 1.12))
elif tip == 15:
    print("Your tip is 15%")
    print("Your total bill is $" + str(Bill * 1.15))

total_bill = str(Bill + (Bill * tip / 100))

split_bills = int(input("How many people are splitting the bill? \n"))
final_payment = round((Bill + (Bill * tip / 100)) / split_bills, 2)
print(f"Each person is to pay ${final_payment}")
