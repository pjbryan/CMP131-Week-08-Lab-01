# PJ Bryan
# CMP-131-80230
# Week 08
# Lab 01
# Assignment 08
# 10/30/2026

# Program table and dividers
divider1 = "*******************"
divider2 = "---------------------------"
print ("LOOP PATTERNS", divider1)

# Pattern A: increasing pattern
print("Pattern A", divider2)
# Rows count up from 1 to 10
for row in range(1, 11):
  # Add one plus sign for each number up to the row number
  plusSign = ""
  for i in range(row):
    plusSign = plusSign + "+"
  print(plusSign)

print()

# Pattern B: decreasing pattern
print("Pattern B", divider2)
# Rows count down from 10 to 1
for row in range(10, 0, -1):
  # Add one plus sign for each number up to the row number
  plusSign = ""
  for i in range(row):
    plusSign = plusSign + "+"
  print(plusSign)