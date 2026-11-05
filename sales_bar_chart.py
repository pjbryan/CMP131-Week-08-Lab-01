# PJ Bryan
# CMP-131-80230
# Week 08
# Lab 01
# Assignment 08
# 10/30/2026

# Program table and dividers
divider1 = "*******************"
divider2 = "---------------------------"
print ("SALES BAR CHART FOR 5 STORES", divider1)

# Variables
store = 5
sales1 = 0
sales2 = 0
sales3 = 0
sales4 = 0
sales5 = 0
asterisk = ""

# Collect and access user input
for storeNumber in range (store):
  sales = float(input(f"Enter today's sales for Store {storeNumber + 1}: "))

  while sales < 0:
    print ("ERROR! Number must be greater or equal to 0.")
    sales = float(input(f"Enter today's sales for Store {storeNumber + 1}: again.: "))

  # Save the sales amount in the matching store variable
  if storeNumber == 0:
    sales1 = sales
  elif storeNumber == 1:
    sales2 = sales
  elif storeNumber == 2:
    sales3 = sales
  elif storeNumber == 3:
    sales4 = sales
  else:
    sales5 = sales

print (divider2)
print ("SALES BAR CHART")
print ("Each * represents $100")

# Display the row of asterisks for each store
for storeNumber in range(store):
  # Get the sales amount for this store
  if storeNumber == 0:
    sales = sales1
  elif storeNumber == 1:
    sales = sales2
  elif storeNumber == 2:
    sales = sales3
  elif storeNumber == 3:
    sales = sales4
  else:
    sales = sales5

  # $100 per asterisk
  numAsterisk = int(sales // 100)

  # A row of asterisks for each store
  asterisk = ""
  for i in range (numAsterisk):
    asterisk = asterisk + "*"

  print (f"Store {storeNumber + 1}: {asterisk}")