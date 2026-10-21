# Banking Management System — Sample Output

This document contains a sample execution of the Python Banking Management System, including account creation, customer details, loan application, locker management, and a money deposit.

> **Privacy note:** The sample output contains personal-looking details, including a name, date of birth, and mobile number. Replace them with fictional test data before publishing this file publicly.

## 1. Main Menu and Account Creation

```text
========== BANK SYSTEM ==========
1. Create Account
2. Apply For Loan
3. Display Customer Details
4. Money Transaction
5. Locker Services
6. Exit
Enter Your Choice: 1

----------- ACCOUNT CREATION -----------
Enter Your Name: Shreehari
Enter Your Gender: Male
Enter Your Age: 23
Enter Your Date Of Birth (DD/MM/YYYY): 10/11/2005
Enter Your Mobile Number: 9284955718
1. Current Account
2. Saving Account
Enter Your Choice: 1
Enter Initial Balance: 8000

-------- CREATION SUCCESSFUL --------
Account Holder: Shreehari
Gender: Male
Account Type: Current
Balance: 8000
Account Number: 744079448966
-------------------------------------
```

## 2. Display Customer Details

```text
========== BANK SYSTEM ==========
1. Create Account
2. Apply For Loan
3. Display Customer Details
4. Money Transaction
5. Locker Services
6. Exit
Enter Your Choice: 3
Enter Your Account Number: 744079448966

================ CUSTOMER DETAILS ================
Account Holder Name:     Shreehari
Holder Age:              23
Current Balance:         Rs. 8000
Account Created:         True
Date Of Birth:           10/11/2005
Mobile Number:           9284955718
Account Type:            Current
Has Loan:                False
Loan Type:               None
Has Locker:              False
==================================================
```

## 3. Loan Application

```text
========== BANK SYSTEM ==========
1. Create Account
2. Apply For Loan
3. Display Customer Details
4. Money Transaction
5. Locker Services
6. Exit
Enter Your Choice: 2

------------ LOAN SECTION ------------
1. Home Loan
2. Car Loan
3. Education Loan
4. Agricultural Loan
Enter Your Choice: 1
Enter Account Number: 744079448966
Enter Account Holder Name: Shreehari
Enter Loan Amount: 500000
Enter Annual Income: 1000000
Repayment Period In Years: 3

-------- LOAN APPLICATION APPROVED --------
Loan Holder: Shreehari
Loan Type: Home Loan
Loan Amount: Rs. 500000
Estimated Monthly Principal: Rs. 13888.89
Repayment Period: 3 years
-------------------------------------------
```

> **Calculation note:** The displayed monthly amount is principal divided by the number of repayment months. It does not include interest, fees, or other lending costs.

## 4. Locker Creation

```text
========== BANK SYSTEM ==========
1. Create Account
2. Apply For Loan
3. Display Customer Details
4. Money Transaction
5. Locker Services
6. Exit
Enter Your Choice: 5

=========== LOCKER SERVICES ===========
1. Create Locker
2. Access Locker
3. Back To Main Menu
Enter Your Choice: 1

---------- LOCKER CREATION ----------
Enter Your Account Number: 744079448966
Enter Account Holder Name: Shreehari
Create A 4-Digit Locker PIN: ****
Confirm Your Locker PIN: ****

-------- LOCKER CREATED SUCCESSFULLY --------
Locker Holder: Shreehari
Locker Number: 529548
Keep Your PIN Secret
----------------------------------------------
```

## 5. Locker Access — Incorrect Details

```text
=========== LOCKER SERVICES ===========
1. Create Locker
2. Access Locker
3. Back To Main Menu
Enter Your Choice: 2

---------- LOCKER ACCESS ----------
Enter Your Account Number: 744079448966
Enter Locker Number: 6525
Enter Locker PIN: ****
Invalid Locker Number Or PIN
```

## 6. Locker Access — Successful Verification

```text
=========== LOCKER SERVICES ===========
1. Create Locker
2. Access Locker
3. Back To Main Menu
Enter Your Choice: 2

---------- LOCKER ACCESS ----------
Enter Your Account Number: 744079448966
Enter Locker Number: 529548
Enter Locker PIN: ****

-------- LOCKER ACCESS GRANTED --------
Locker Holder: Shreehari
Locker Number: 529548
Locker Status: OPEN
---------------------------------------
```

## 7. Deposit Money

```text
========== BANK SYSTEM ==========
1. Create Account
2. Apply For Loan
3. Display Customer Details
4. Money Transaction
5. Locker Services
6. Exit
Enter Your Choice: 4

--------- MONEY TRANSACTION ---------
1. Deposit Money
2. Withdraw Money
3. Transfer Money
Enter Your Choice: 1
Enter Your Account Number: 744079448966
Enter Deposit Amount: 7500
Deposit Successful
Available Balance: Rs. 15500
```

## 8. Customer Details After Loan and Locker Creation

```text
========== BANK SYSTEM ==========
1. Create Account
2. Apply For Loan
3. Display Customer Details
4. Money Transaction
5. Locker Services
6. Exit
Enter Your Choice: 3
Enter Your Account Number: 744079448966

================ CUSTOMER DETAILS ================
Account Holder Name:     Shreehari
Holder Age:              23
Current Balance:         Rs. 15500
Account Created:         True
Date Of Birth:           10/11/2005
Mobile Number:           9284955718
Account Type:            Current
Has Loan:                True
Loan Type:               Home Loan
Has Locker:              True
Locker Number:           529548
==================================================
```

## 9. Exit

```text
========== BANK SYSTEM ==========
1. Create Account
2. Apply For Loan
3. Display Customer Details
4. Money Transaction
5. Locker Services
6. Exit
Enter Your Choice: 6
Thank You For Banking With Us!

Process finished with exit code 0
```

## Features Demonstrated

- Account creation and account number generation
- Customer record storage and retrieval
- Loan application and basic eligibility calculation
- Locker creation and PIN verification
- Deposit transaction and balance update
- Customer details reflecting updated loan and locker status
- Menu navigation and graceful exit

## Disclaimer

This is a training project intended for educational purposes. It is not a production banking system. Customer data is held in memory, the sample loan calculation is simplified, and the locker PIN implementation is not suitable for real-world security.

**Training acknowledgement:** Developed as part of Python training conducted by Rubicon under the guidance of **Prof. Vipul Mahindrakar, Training and Placement Head**.
