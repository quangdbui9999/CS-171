
'''
import math

def doubleInvestment(investment, rate):
    return math.ceil(math.log(2) / math.log(1 + rate))

initInvest = int(input("Enter your initial investment: "))
rate = float(input("Enter the annualized interest rate (ex. 0.02): "))
print("Result: %f." %doubleInvestment(initInvest, rate))
'''


def input_float(number):
    valid = False
    while not valid:
        try:
            x = input(number)
            x = float(x)
            return x
        except ValueError as e:
            valid = False


def doubleInvestment(annual_interest_rate, initialized_investment):
    double_money = initialized_investment * 2
    count_year = 0
    exit_loop = True
    while exit_loop:
        annual_money = initialized_investment * annual_interest_rate
        initialized_investment += annual_money
        count_year += 1
        if double_money <= initialized_investment:
            exit_loop = False
    return count_year


money = input_float("Enter the initialized investment: ")
interest_rate = input_float("Enter the interest rate: ")
years = doubleInvestment(interest_rate, money)
print("After %d year, your money is doubled." % years)
