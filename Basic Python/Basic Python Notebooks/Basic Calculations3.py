name = input('Enter customer name :')
tax = 10
tbt = float(input('The bill total:'))
tax_to_pay = tbt*tax/100
total = format(tbt + tax_to_pay, '.2f')
print(f"Name:{name} \nTotal:{tbt} \nTax:{tax_to_pay}\nTotal:{total}")