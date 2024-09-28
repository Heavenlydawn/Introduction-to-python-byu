print('Rating from 1 -10 with 1 being the lowest and 10 being the highest answer the following questions')
print()
loan_size = float(input('How large is the loan? '))
credit_score = float(input('How good is your credit score? '))
income = float(input('How high is your income? '))
down_payment = float(input('How large is your down payment? '))

should_loan = False

if loan_size >= 5:
    if credit_score >= 7 and income >= 7:
        should_loan = True
    elif credit_score >= 7 or income >= 7:
        if down_payment >= 5:
            should_loan = True
    else:
        should_loan = False
else:
    if credit_score < 4:
      should_loan = False
    else:
        if income >= 7 or down_payment >= 7:
            should_loan = True
        elif income >= 4 or down_payment >= 4:
            should_loan = True
        else:
            should_loan = False

if should_loan:
    print('The decision is YES. This is a good loan. ')
else:
    print('The decision is no. You should not loan this money')