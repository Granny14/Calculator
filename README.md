Finance Calculators
This project provides a program that allows users to access two different financial calculators: an investment calculator and a home loan repayment calculator.

Objectives
The program offers the following functionalities:

Investment Calculator
Home Loan Repayment Calculator
Getting Started
Prerequisites
Ensure you have Python installed on your system. This project is compatible with Python 3.x.

Installation
Clone this repository to your local machine using:

bash
Copy code
git clone https://github.com/your-username/finance_calculators.git
Usage
Navigate to the project directory:

bash
Copy code
cd finance_calculators
Run the program:

bash
Copy code
python finance_calculators.py
Follow the on-screen prompts to use the calculators.

Features
1. Investment Calculator
Prompts the user to input:

The amount of money to be deposited.
The interest rate (as a percentage, e.g., 8 for 8%).
The number of years for the investment.
The type of interest: "simple" or "compound".
Uses the following formulas to calculate the total amount:

Simple Interest: 
𝐴
=
𝑃
(
1
+
𝑟
×
𝑡
)
A=P(1+r×t)
Compound Interest: 
𝐴
=
𝑃
×
(
1
+
𝑟
)
𝑡
A=P×(1+r) 
t
 
Where:

𝑟
r is the interest rate divided by 100.
𝑃
P is the principal amount.
𝑡
t is the number of years.
𝐴
A is the total amount after applying the interest.
2. Home Loan Repayment Calculator
Prompts the user to input:

The present value of the house.
The annual interest rate (as a percentage).
The number of months for repayment.
Uses the following formula to calculate the monthly repayment amount:

𝑥
=
𝑖
×
𝑃
1
−
(
1
+
𝑖
)
−
𝑛
x= 
1−(1+i) 
−n
 
i×P
​
 
Where:

𝑃
P is the present value of the house.
𝑖
i is the monthly interest rate (annual rate divided by 12).
𝑛
n is the number of months for repayment.
Example
plaintext
Copy code
Choose either 'investment' or 'bond' to proceed:
investment

Enter the amount to deposit:
1000
Enter the interest rate (e.g., 8 for 8%):
8
Enter the number of years:
10
Do you want 'simple' or 'compound' interest:
compound

The total amount after 10 years with compound interest is: 2158.92
Contributing
Feel free to fork this repository, make enhancements, and submit pull requests.

License
This project is licensed under the MIT License.
