
import random

customer_details = []

NAME = 0
AGE = 1
BALANCE = 2
ACCOUNT_CREATED = 3
DOB = 4
MOBILE = 5
ACCOUNT_TYPE = 6
HAS_LOAN = 7
LOAN_TYPE = 8
HAS_LOCKER = 9
LOCKER_NUMBER = 10
LOCKER_PIN = 11


def findCustomer(acc_number):
    for customer in customer_details:
        if acc_number in customer:
            return customer
    return None


def generateAccountNumber():
    while True:
        acc_number = random.randint(100000000000, 999999999999)
        if findCustomer(acc_number) is None:
            return acc_number


def createAccount():
    print('\n----------- ACCOUNT CREATION -----------')

    cust_name = input('Enter Your Name: ')
    cust_gender = input('Enter Your Gender: ')
    cust_age = int(input('Enter Your Age: '))

    if cust_age < 18:
        print('You Are Underage To Open An Account')
        return

    cust_dob = input('Enter Your Date Of Birth (DD/MM/YYYY): ')
    cust_mobile = input('Enter Your Mobile Number: ')

    print('1. Current Account')
    print('2. Saving Account')
    choice = int(input('Enter Your Choice: '))

    if choice == 1:
        account_type = 'Current'
        minimum_balance = 5000
    elif choice == 2:
        account_type = 'Saving'
        minimum_balance = 1000
    else:
        print('Invalid Account Type')
        return

    initial_balance = int(input('Enter Initial Balance: '))

    if initial_balance < minimum_balance:
        print(f'Minimum Balance Required: {minimum_balance}')
        return

    acc_number = generateAccountNumber()

    temp_cust_details = [
        cust_name,
        cust_age,
        initial_balance,
        True,
        cust_dob,
        cust_mobile,
        account_type,
        False,
        'None',
        False,
        None,
        None
    ]

    customer_details.append({acc_number: temp_cust_details})

    print('\n-------- CREATION SUCCESSFUL --------')
    print('Account Holder:', cust_name)
    print('Gender:', cust_gender)
    print('Account Type:', account_type)
    print('Balance:', initial_balance)
    print('Account Number:', acc_number)
    print('-------------------------------------')


def displayCustomerDetails():
    acc_confirm = int(input('Enter Your Account Number: '))
    customer = findCustomer(acc_confirm)

    if customer is None:
        print('Account Number Not Found')
        return

    details = customer[acc_confirm]

    print('\n================ CUSTOMER DETAILS ================')
    print(f"{'Account Holder Name:':<24} {details[NAME]}")
    print(f"{'Holder Age:':<24} {details[AGE]}")
    print(f"{'Current Balance:':<24} Rs. {details[BALANCE]}")
    print(f"{'Account Created:':<24} {details[ACCOUNT_CREATED]}")
    print(f"{'Date Of Birth:':<24} {details[DOB]}")
    print(f"{'Mobile Number:':<24} {details[MOBILE]}")
    print(f"{'Account Type:':<24} {details[ACCOUNT_TYPE]}")
    print(f"{'Has Loan:':<24} {details[HAS_LOAN]}")
    print(f"{'Loan Type:':<24} {details[LOAN_TYPE]}")
    print(f"{'Has Locker:':<24} {details[HAS_LOCKER]}")

    if details[HAS_LOCKER]:
        print(f"{'Locker Number:':<24} {details[LOCKER_NUMBER]}")

    print('==================================================')


def applyLoan():
    print('\n------------ LOAN SECTION ------------')
    print('1. Home Loan')
    print('2. Car Loan')
    print('3. Education Loan')
    print('4. Agricultural Loan')

    loan_options = {
        1: 'Home Loan',
        2: 'Car Loan',
        3: 'Education Loan',
        4: 'Agricultural Loan'
    }

    loan_choice = int(input('Enter Your Choice: '))

    if loan_choice not in loan_options:
        print('Invalid Loan Type')
        return

    loan_type = loan_options[loan_choice]

    acc_confirm = int(input('Enter Account Number: '))
    customer = findCustomer(acc_confirm)

    if customer is None:
        print('Account Number Not Found')
        return

    details = customer[acc_confirm]

    if details[HAS_LOAN]:
        print('You Already Have A Loan')
        print('Existing Loan:', details[LOAN_TYPE])
        return

    acc_name = input('Enter Account Holder Name: ')

    if acc_name.strip().lower() != details[NAME].strip().lower():
        print('Account Holder Name Does Not Match')
        return

    loan_amount = int(input('Enter Loan Amount: '))
    annual_income = int(input('Enter Annual Income: '))
    total_loan_year = int(input('Repayment Period In Years: '))

    if loan_amount <= 0 or annual_income <= 0 or total_loan_year <= 0:
        print('Enter Valid Positive Amounts And Years')
        return

    monthly_repayment = loan_amount / (total_loan_year * 12)
    monthly_salary = annual_income / 12
    half_salary = monthly_salary / 2

    if monthly_repayment <= half_salary:
        details[HAS_LOAN] = True
        details[LOAN_TYPE] = loan_type

        print('\n-------- LOAN APPLICATION APPROVED --------')
        print('Loan Holder:', details[NAME])
        print('Loan Type:', loan_type)
        print('Loan Amount: Rs.', loan_amount)
        print('Estimated Monthly Principal: Rs.',
              round(monthly_repayment, 2))
        print('Repayment Period:', total_loan_year, 'years')
        print('-------------------------------------------')
    else:
        print('Loan Eligibility Criteria Not Met')


def moneyTransaction():
    print('\n--------- MONEY TRANSACTION ---------')
    print('1. Deposit Money')
    print('2. Withdraw Money')
    print('3. Transfer Money')

    choice = int(input('Enter Your Choice: '))
    acc_number = int(input('Enter Your Account Number: '))

    customer = findCustomer(acc_number)

    if customer is None:
        print('Account Number Not Found')
        return

    details = customer[acc_number]

    if choice == 1:
        amount = int(input('Enter Deposit Amount: '))

        if amount <= 0:
            print('Enter A Valid Amount')
            return

        details[BALANCE] += amount
        print('Deposit Successful')

    elif choice == 2:
        amount = int(input('Enter Withdrawal Amount: '))

        if amount <= 0:
            print('Enter A Valid Amount')
            return

        if amount > details[BALANCE]:
            print('Insufficient Balance')
            return

        details[BALANCE] -= amount
        print('Withdrawal Successful')

    elif choice == 3:
        receiver_acc = int(input('Enter Receiver Account Number: '))
        receiver = findCustomer(receiver_acc)

        if receiver is None:
            print('Receiver Account Not Found')
            return

        if receiver_acc == acc_number:
            print('Cannot Transfer Money To The Same Account')
            return

        amount = int(input('Enter Transfer Amount: '))

        if amount <= 0:
            print('Enter A Valid Amount')
            return

        if amount > details[BALANCE]:
            print('Insufficient Balance')
            return

        receiver_details = receiver[receiver_acc]

        details[BALANCE] -= amount
        receiver_details[BALANCE] += amount

        print('Money Transfer Successful')
        print('Receiver:', receiver_details[NAME])

    else:
        print('Invalid Transaction Choice')
        return

    print('Available Balance: Rs.', details[BALANCE])


def createLocker():
    print('\n---------- LOCKER CREATION ----------')

    acc_number = int(input('Enter Your Account Number: '))
    customer = findCustomer(acc_number)

    if customer is None:
        print('Account Number Not Found')
        return

    details = customer[acc_number]

    if details[HAS_LOCKER]:
        print('You Already Have A Locker')
        print('Locker Number:', details[LOCKER_NUMBER])
        return

    acc_name = input('Enter Account Holder Name: ')

    if acc_name.strip().lower() != details[NAME].strip().lower():
        print('Account Holder Name Does Not Match')
        return

    pin = input('Create A 4-Digit Locker PIN: ')

    if len(pin) != 4 or not pin.isdigit():
        print('PIN Must Contain Exactly 4 Digits')
        return

    confirm_pin = input('Confirm Your Locker PIN: ')

    if pin != confirm_pin:
        print('PINs Do Not Match')
        return

    locker_number = random.randint(100000, 999999)

    existing_lockers = [
        c[acc][LOCKER_NUMBER]
        for c in customer_details
        for acc in c
        if c[acc][HAS_LOCKER]
    ]

    while locker_number in existing_lockers:
        locker_number = random.randint(100000, 999999)

    details[HAS_LOCKER] = True
    details[LOCKER_NUMBER] = locker_number
    details[LOCKER_PIN] = pin

    print('\n-------- LOCKER CREATED SUCCESSFULLY --------')
    print('Locker Holder:', details[NAME])
    print('Locker Number:', locker_number)
    print('Keep Your PIN Secret')
    print('----------------------------------------------')


def accessLocker():
    print('\n---------- LOCKER ACCESS ----------')

    acc_number = int(input('Enter Your Account Number: '))
    customer = findCustomer(acc_number)

    if customer is None:
        print('Account Number Not Found')
        return

    details = customer[acc_number]

    if not details[HAS_LOCKER]:
        print('No Locker Found For This Account')
        print('Please Create A Locker First')
        return

    locker_number = int(input('Enter Locker Number: '))
    pin = input('Enter Locker PIN: ')

    if (locker_number == details[LOCKER_NUMBER]
            and pin == details[LOCKER_PIN]):
        print('\n-------- LOCKER ACCESS GRANTED --------')
        print('Locker Holder:', details[NAME])
        print('Locker Number:', details[LOCKER_NUMBER])
        print('Locker Status: OPEN')
        print('---------------------------------------')
    else:
        print('Invalid Locker Number Or PIN')

def lockerMenu():
    while True:
        print('\n=========== LOCKER SERVICES ===========')
        print('1. Create Locker')
        print('2. Access Locker')
        print('3. Back To Main Menu')

        choice = input('Enter Your Choice: ')

        match choice:
            case '1':
                createLocker()
            case '2':
                accessLocker()
            case '3':
                break
            case _:
                print('Invalid Choice')

def welcome():
    while True:
        print('\n========== BANK SYSTEM ==========')
        print('1. Create Account')
        print('2. Apply For Loan')
        print('3. Display Customer Details')
        print('4. Money Transaction')
        print('5. Locker Services')
        print('6. Exit')

        customer_choice = input('Enter Your Choice: ')

        match customer_choice:
            case '1':
                createAccount()
            case '2':
                applyLoan()
            case '3':
                displayCustomerDetails()
            case '4':
                moneyTransaction()
            case '5':
                lockerMenu()
            case '6':
                print('Thank You For Banking With Us!')
                break
            case _:
                print('Invalid Choice. Please Try Again.')


welcome()
