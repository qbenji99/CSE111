from datetime import datetime

### Variables
sales_tax = .06
discount = 0
current = datetime.now()
weekday = current.isoweekday()
weekday = 2

answer = ""
subtotal_tax = subtotal * sales_tax
### Variables

while answer.lower() != "done":
  subtotal = float(input("Please enter the subtotal: "))
  quantity = int(input("How many? "))
  subtotal *= quantity
  
  answer = input("Are you done with stuff?: ")

if 2 <= weekday <= 3 and subtotal >= 50:
  discount = (subtotal * .1)
  subtotal_tax = (subtotal - discount) * sales_tax
  print(f"The discount is: ${discount:.2f}")
elif 2 <= weekday <= 3 and subtotal <= 50:
  difference = 50 - subtotal
  print(f"You need ${difference:.2f} in order to receive the discount!")

print(f"The sales tax is: ${subtotal_tax:.2f}")
print(f"The total is ${(subtotal + subtotal_tax - discount):.2f}")