'''
# Assignment-2 - Paying Debt off in a Year
# Now write a program that calculates the minimum fixed monthly
payment needed in order pay off a credit card balance within 12 months.
# By a fixed monthly payment, we mean a single number which does not change
each month, but instead is a constant amount that will be
# paid each month.
# In this problem, we will not be dealing with a minimum monthly payment rate.
# The following variables contain values as described below:
# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal
# The program should print out one line: the lowest monthly payment that will
pay off all debt in under 1 year, for example:
# Lowest Payment: 180
# Assume that the interest is compounded monthly according to the balance at the
end of the month (after the payment for that month is
# made).
# The monthly payment must be a multiple of $10 and is the same for all months.
Notice that it is possible for the balance to become
# negative using this payment scheme, which is okay. A summary of the required math
is found below:
# Monthly interest rate = (Annual interest rate) / 12.0
# Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x
Monthly unpaid balance)
@author: gangadharsingh
'''
def paying_debt(balance, annual_ir):
    '''checking the condition
    '''
    if balance < 0:
        return 0
    i_inp = 10
    while True:
        var_a = 0
        bal_b = balance
        while var_a != 12:
            unbal_a = bal_b - (i_inp)
            bal_b = unbal_a + (unbal_a * annual_ir/12)
            var_a += 1
        if bal_b <= 0.5:
            break
        i_inp += 10
    return i_inp

def main():
    '''checking the input value
    '''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Lowest Payment:",paying_debt(data[0], data[1]))
    
if __name__ == "__main__":
    main()
