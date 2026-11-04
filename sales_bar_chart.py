# PJ Bryan
# CMP-131-80230
# Week 08
# Lab 01
# Assignment 08
# 10/30/2026

# Program table and dividers
divider1 = "*******************"
divider2 = "---------------------------"
print ("SALES BAR CHART", divider1)

store = int(input("Enter number of stores: "))

for storeNumber in range (store):
  sales = int(input(f"Enter today's sales for Store {storeNumber + 1}: "))
  if sales <= 0:
    print ("ERROR! Sales must be a positive number.")
    sales = sales / 100
  asterisk = ""
  for salesNumber in range(sales):
    asterisk = asterisk + "*"
    asterisk = asterisk + "/n"

print (f"Store {storeNumber + 1}: {asterisk}")