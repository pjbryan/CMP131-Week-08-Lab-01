# CMP 131 – Python Programming


> **Required file location:** Keep every Python file directly in the repository root. Do not create a `src` folder.

## Week 8 – Lab 1: Sales Bar Chart and Loop Patterns

**Total Points: 100**

* Program 1: Sales Bar Chart — 50 points
* Program 2: Increasing and Decreasing Patterns — 50 points

## Learning Objectives

After completing this lab, students should be able to:

* Accept and convert numeric user input.
* Use loops to repeat input and output operations.
* Use counter-controlled loops.
* Use nested loops to create visual patterns.
* Use integer division to convert sales amounts into chart symbols.
* Control whether output continues on the same line or moves to a new line.
* Validate numeric input.
* Display information in a clear, organized format.
* Test programs using different input values.
* Use comments to explain the major sections of a program.

## Assignment Overview

Create two separate Python programs using loops.

The first program asks the user to enter the daily sales for five stores and displays a horizontal bar chart. Each asterisk in the chart represents `$100` in sales.

The second program uses loops to display two patterns. Pattern A increases from one plus sign to ten plus signs. Pattern B decreases from ten plus signs to one plus sign.

Create the following Python files:

* `sales_bar_chart.py`
* `loop_patterns.py`

The instructor is not providing completed Python code or an exact output design. Students must design, write, and test their own programs.

# Program 1: Sales Bar Chart

**Points: 50**

## Program Description

Create a program that asks the user to enter today’s sales for five stores.

After receiving all five sales amounts, the program must display a horizontal bar chart comparing the stores’ sales.

Each asterisk must represent `$100` in sales.

For example:

* `$100` produces one asterisk.
* `$500` produces five asterisks.
* `$1,000` produces ten asterisks.
* `$1,900` produces nineteen asterisks.

## Required Python File

Create a Python file named:

`sales_bar_chart.py`

Include a comment header containing:

* Student name
* Course number
* Week number
* Lab number
* Assignment title
* Date

## Part 1: Display a Program Title

Display a descriptive title when the program begins.

The title should clearly indicate that the program creates a sales bar chart for five stores.

Students should create their own title and output design.

## Part 2: Enter the Store Sales

Ask the user to enter today’s sales for each of the five stores.

The program must collect sales amounts for:

* Store 1
* Store 2
* Store 3
* Store 4
* Store 5

Each prompt must clearly identify the store.

Examples:

* Enter today’s sales for Store 1
* Enter today’s sales for Store 2

Continue until sales amounts have been entered for all five stores.

## Part 3: Convert and Validate the Input

Convert each sales amount to an appropriate numeric data type before using it in a calculation.

A sales amount:

* May be zero.
* Must not be negative.
* May be entered as a whole number or decimal value.

If the user enters a negative sales amount:

* Display an appropriate error message.
* Ask the user to enter the sales amount again.
* Do not accept the negative value.

Use meaningful variable names throughout the program.

## Part 4: Determine the Number of Asterisks

Each asterisk represents `$100` in sales.

Determine the number of asterisks for each store by dividing its sales amount by `100`.

The number of asterisks must be a whole number because a loop cannot repeat a fractional number of times.

Only complete groups of `$100` should produce an asterisk.

Examples:

| Sales Amount | Number of Asterisks |
| -----------: | ------------------: |
|           $0 |                   0 |
|         $100 |                   1 |
|         $500 |                   5 |
|         $550 |                   5 |
|       $1,000 |                  10 |
|       $1,250 |                  12 |

A partial `$100` does not produce an additional asterisk.

## Part 5: Display the Chart Heading

Before displaying the bars, print a chart heading that includes:

* A descriptive chart title
* An explanation that each asterisk represents `$100`

For example:

```text
SALES BAR CHART
Each * represents $100
```

Students may create their own wording and formatting.

## Part 6: Display the Sales Bars

Display one labeled bar for each store.

Each bar must:

* Begin with the store number.
* Contain the correct number of asterisks.
* Appear on a separate line.
* Be created using a loop.

The program should display a structure similar to the following:

```text
Store 1: **********
Store 2: ************
Store 3: ******************
Store 4: ********
Store 5: *******************
```

Do not manually type the asterisks shown in the bar chart. The number of asterisks must be determined from the entered sales amount.

## Loop Requirements

The program must use loops to create the bars.

When displaying an individual bar:

* Use a loop to print the required number of asterisks.
* Keep the asterisks for that store on the same output line.
* Move to a new line before displaying the next store.

Students may use techniques covered in class to organize the five sales amounts.

## Required Testing for Program 1

### Test 1: Assignment Example

Enter the following sales amounts:

|   Store |  Sales |
| ------: | -----: |
| Store 1 | $1,000 |
| Store 2 | $1,200 |
| Store 3 | $1,800 |
| Store 4 |   $800 |
| Store 5 | $1,900 |

Expected number of asterisks:

|   Store | Asterisks |
| ------: | --------: |
| Store 1 |        10 |
| Store 2 |        12 |
| Store 3 |        18 |
| Store 4 |         8 |
| Store 5 |        19 |

### Test 2: Zero Sales

Enter `0` for one of the stores.

Confirm that:

* The program accepts the value.
* The store label is displayed.
* No asterisks are displayed for that store.
* The program continues without an error.

### Test 3: Amount Not Divisible by 100

Enter `550` for one of the stores.

Confirm that five asterisks are displayed.

### Test 4: Negative Sales

First enter:

`-100`

Confirm that:

* An error message is displayed.
* The negative value is rejected.
* The program asks for the sales amount again.

Then enter a valid value and confirm that the program continues.

## Program 1 Point Distribution

* Program title and clear prompts: 5 points
* Correctly collect sales for five stores: 10 points
* Correct numeric conversion: 5 points
* Negative-sales validation: 5 points
* Correct conversion from sales to asterisks: 10 points
* Correct use of loops to create the bars: 10 points
* Clear chart formatting, comments, and testing: 5 points

**Program 1 Total: 50 points**

# Program 2: Increasing and Decreasing Loop Patterns

**Points: 50**

## Program Description

Create a program that displays two patterns using loops.

Pattern A increases from one plus sign to ten plus signs.

Pattern B decreases from ten plus signs to one plus sign.

The program must display Pattern A first, followed by Pattern B.

## Required Python File

Create a Python file named:

`loop_patterns.py`

Include a comment header containing:

* Student name
* Course number
* Week number
* Lab number
* Assignment title
* Date

## Part 1: Display a Program Title

Display a descriptive program title.

The title should indicate that the program creates increasing and decreasing patterns using loops.

## Part 2: Display Pattern A

Use loops to display the following increasing pattern:

```text
+
++
+++
++++
+++++
++++++
+++++++
++++++++
+++++++++
++++++++++
```

Pattern A must:

* Begin with one plus sign.
* Contain ten rows.
* Add one plus sign to each new row.
* End with ten plus signs.
* Be created using loops.

Do not manually write ten separate `print()` statements.

## Part 3: Display Pattern B

After Pattern A, display an appropriate heading and then use loops to create the following decreasing pattern:

```text
++++++++++
+++++++++
++++++++
+++++++
++++++
+++++
++++
+++
++
+
```

Pattern B must:

* Begin with ten plus signs.
* Contain ten rows.
* Remove one plus sign from each new row.
* End with one plus sign.
* Be created using loops.

Do not manually write ten separate `print()` statements.

## Part 4: Use Nested Loops

Use nested loops for each pattern.

An outer loop should control:

* The number of rows.
* Whether the current row is increasing or decreasing in length.

An inner loop should control:

* The number of plus signs displayed on the current row.

The plus signs for one row must remain on the same line. After the inner loop finishes, move the output to the next line.

## Part 5: Separate the Patterns

Clearly identify the two patterns with headings.

For example:

```text
Pattern A
```

and:

```text
Pattern B
```

Include appropriate blank lines so the two patterns are easy to distinguish.

## Required Testing for Program 2

### Pattern A Testing

Confirm that:

* The first row contains one plus sign.
* The second row contains two plus signs.
* Each new row contains one additional plus sign.
* The tenth row contains ten plus signs.
* Exactly ten rows are displayed.

### Pattern B Testing

Confirm that:

* The first row contains ten plus signs.
* The second row contains nine plus signs.
* Each new row contains one fewer plus sign.
* The tenth row contains one plus sign.
* Exactly ten rows are displayed.

### Complete Program Testing

Confirm that:

* Pattern A appears before Pattern B.
* Both patterns have descriptive headings.
* The plus signs on each row remain on the same line.
* Each pattern contains exactly ten rows.
* Loops create both patterns.
* No pattern row is manually typed.
* The program runs without errors.

## Program 2 Point Distribution

* Program title and pattern headings: 5 points
* Correct outer loop for Pattern A: 10 points
* Correct inner loop for Pattern A: 10 points
* Correct outer loop for Pattern B: 10 points
* Correct inner loop for Pattern B: 10 points
* Clear formatting, comments, and successful testing: 5 points

**Program 2 Total: 50 points**

# Code Comments

Use comments to identify and explain the major sections of both programs.

Include comments for:

* The program information header
* The program title
* Variable initialization
* User input
* Input validation
* Sales-to-asterisk conversion
* Chart output
* Pattern A loops
* Pattern B loops
* Final output

Comments should briefly explain the purpose of each major section. They do not need to repeat every Python statement word for word.

# Functional Requirements

## Sales Bar Chart Program

When `sales_bar_chart.py` runs, it must:

* Display a descriptive program title.
* Ask for today’s sales for five stores.
* Clearly identify each store in the input prompts.
* Convert each sales amount to an appropriate numeric data type.
* Accept zero as a valid sales amount.
* Reject negative sales amounts.
* Use `$100` for each asterisk.
* Display only complete groups of `$100`.
* Display a labeled bar for each store.
* Use loops to generate the asterisks.
* Keep each store’s bar on one line.
* Display all five store bars.
* Run without errors.

## Loop Patterns Program

When `loop_patterns.py` runs, it must:

* Display a descriptive program title.
* Display a heading for Pattern A.
* Use nested loops to create Pattern A.
* Increase Pattern A from one through ten plus signs.
* Display a heading for Pattern B.
* Use nested loops to create Pattern B.
* Decrease Pattern B from ten through one plus sign.
* Display exactly ten rows in each pattern.
* Avoid manually typing the individual rows.
* Run without errors.

# General Requirements

* Use Python to complete both programs.
* Create both required Python files.
* Use meaningful and consistent variable names.
* Convert user input to an appropriate numeric data type.
* Use loops where required.
* Use nested loops to create both patterns.
* Do not manually type the chart bars or pattern rows.
* Include a complete comment header in both files.
* Include comments explaining the major sections.
* Use clear prompts, headings, and output labels.
* Test both programs using all required test cases.
* Check spelling, capitalization, grammar, and punctuation.
* Make sure both programs run without errors.
* Follow the course AI-use policy.
* Record any AI assistance in `AI-Use-Report.md`.

# Required Organization

Organize the assignment as follows:

* `Week-08`

  * `Lab-01`

    * `CMP131-Week-08-Lab-01.md`
    * `AI-Use-Report.md`
    * `src`

      * `sales_bar_chart.py`
      * `loop_patterns.py`

# Submission Requirements

Submit or push the complete `Lab-01` folder.

The submission must include:

* `sales_bar_chart.py`
* `loop_patterns.py`
* `AI-Use-Report.md`

Before submitting, verify that:

* Both required Python files are included.
* Both filenames are correct.
* Both programs contain a complete comment header.
* Both programs contain comments explaining the major sections.
* The sales program asks for sales from five stores.
* Negative sales amounts are rejected.
* Each asterisk represents `$100`.
* All five store bars are displayed correctly.
* The bars are generated using loops.
* Pattern A increases from one to ten plus signs.
* Pattern B decreases from ten to one plus sign.
* Each pattern contains exactly ten rows.
* Both patterns use nested loops.
* The pattern rows are not manually typed.
* Both programs were tested using the required values.
* Both programs run without errors.
* The AI-use report is complete.
* The latest work has been committed and pushed to GitHub.

# Suggested Git Commit Messages

* Create Week 8 Lab 1 Python files
* Add five-store sales input
* Add sales input validation
* Create sales bar chart loops
* Test sales-to-asterisk conversion
* Add increasing Pattern A
* Add decreasing Pattern B
* Test nested loop patterns
* Improve output formatting and comments
* Complete Week 8 Python lab

---

## GitHub Starter Repository

Use the following public starter repository:

[CMP131-Week-08-Lab-01](https://github.com/ahedhli12/CMP131-Week-08-Lab-01)

### Getting Started

1. Open the starter repository using the link above.
2. Select **Use this template → Create a new repository** when the template option is available.
3. Choose your personal GitHub account as the owner.
4. Name your repository `LastName-FirstName-CMP131-Week-08-Lab-01`.
5. Set your repository to **Public**.
6. Clone your own newly created repository—not the instructor’s starter repository.
7. Open the entire cloned folder in Visual Studio Code.
8. Complete and test every required Python file.
9. Commit and push your work to GitHub.
10. Verify that your latest files appear on GitHub.
11. Complete `AI-Use-Report.md`.
12. Submit the required work through Blackboard Ultra and include your public repository link when requested.

### Required Repository Files

- `CMP131-Week-08-Lab-01.md`
- `AI-Use-Policy.md`
- `AI-Use-Report.md`
- `loop_patterns.py`
- `sales_bar_chart.py`

### Before You Submit

- [ ] All required Python files are in the repository root.
- [ ] Every required filename is exact.
- [ ] Each program runs successfully.
- [ ] Required tests and screenshots are complete.
- [ ] `AI-Use-Report.md` is complete and accurate.
- [ ] The latest commit is visible on GitHub.
