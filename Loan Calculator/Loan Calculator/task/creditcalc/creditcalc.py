import sys
import math
import argparse

# loan_principal = 'Loan principal: 1000'
# final_output = 'The loan has been repaid!'
# first_month = 'Month 1: repaid 250'
# second_month = 'Month 2: repaid 250'
# third_month = 'Month 3: repaid 500'
# arg = sys.argv
# loan_principal = annuity_payment / ((i * math.pow(1 + i, number_periods)) / (math.pow(1 + i, number_periods) - 1))
# write your code here
from typing import Any


def main():
    print('What do you want to calculate?\n'
          'Type "n"  for number of monthly payments,\n'
          'Type "a" for annuity monthly payment amount,\n'
          'Type "p" for loan principle:')


parser = argparse.ArgumentParser(description='This allows you to enter the information you have')
parser.add_argument('--type', type=str,
                    choices=['annuity', 'diff'],
                    help='You can only choose one')
parser.add_argument('--principal', type=int,
                    help='Principal of the loan')
parser.add_argument('--payment', type=int,
                    help='Enter monthly payment')
parser.add_argument('--periods', type=int,
                    help='The number of months needed to repay the loan')
parser.add_argument('--interest', type=float,
                    help='Enter interest rate in percents')


args = parser.parse_args()
choice = args.type
a = args.principal
b = args.periods
if args.interest is None:
    print("Incorrect parameters")
    exit()
else:
    c = args.interest

d = args.payment
i = c / (12 * 100)


class Calc:
    def __init__(self, a, b, c):    
        self.a = a
        self.b = b
        self.c = c
        
    def calc_diff(pr, nu, i):
        p = pr
        n = nu
        li = []
        for num in range(1, n + 1):
            diff = (p / n) + i * (p - (p * ((num - 1) / n)))
            print(f"Month {num} Payment is {math.ceil(diff)}")
            li.append(math.ceil(diff))
        xi = sum(li)
        o = int(xi) - p
        print("\n",
              f"Overpayment = {o}")

    def calc_annuity(a, b, i):
        an = a * ((i * math.pow((1 + i), b)) / (math.pow((1 + i), b) - 1))
        ov = (math.ceil(an) * b) - a
        print(f"Correct loan Annuity is {math.ceil(an)}\n"
              f'Overpayment = {math.ceil(ov)}')

    def calc_prn(pa, nu, i):
        p = pa / ((i * pow((1 + i), nu)) / (pow((1+i), nu) - 1))
        ov = (pa * nu) - p
        print(f"Your loan principal = {math.floor(p)}")
        print(f"Overpayment = {math.ceil(ov)}")

    def length(p, a, i):
        x = a / (a - i * p)
        base = 1 + i
        num_month = math.log(x, base)
        n = num_month
        ov = (a * math.ceil(n)) - p
        y, m = divmod(math.ceil(n), 12)
        print(f"It will take {y} years to repay this loan\n"
              f'Overpayment = {math.ceil(ov)}')


"""
def calc_diff(a, b, i):
    p = a
    n = b
    li = []
    for num in range(1, n + 1):
        diff = (p / n) + i * (p - (p * ((num - 1) / n)))
        li.append(math.ceil(diff))
        print(f"Month {num} Payment is {math.ceil(diff)}")
    xi = sum(li)
    o = int(xi) - p
    print("\n",
          f"Overpayment = {o}")


def calc_annuity(a, b, i):
    an = a * ((i * math.pow((1 + i), b)) / (math.pow((1 + i), b) - 1))
    ov = (math.ceil(an) * b) - a
    print(f"Correct loan Annuity is {math.ceil(an)}\n"
          f'Overpayment = {math.ceil(ov)}')


def calc_prn(pa, nu, i):
    p = pa / ((i * pow((1 + i), nu)) / (pow((1+i), nu) - 1))
    ov = (pa * nu) - p
    print(f"Your loan principal = {math.floor(p)}\n"
          f"Overpayment = {math.ceil(ov)}")


def length(prn, pa, i):
    x = pa / (pa - (i * prn))
    base = 1 + i
    num_month = math.log(x, base)
    n = num_month
    ov = (pa * math.ceil(n)) - prn
    y, m = divmod(math.ceil(n), 12)
    print(f"It will take {y} years to repay this loan\n"
          f'Overpayment = {math.ceil(ov)}')
"""

if args.type != 'annuity' and choice != 'diff':
    print("Incorrect parameters")
elif args.type == "diff" and args.payment is not None:
    print("Incorrect parameters")
elif len(sys.argv) < 5:
    print("Incorrect parameters")
elif args.interest is None:
    print("Incorrect parameters")
else:
    pass


if args.type == "diff" and args.payment is None:
    Calc.calc_diff(a, b, i)
elif args.type == "annuity" and d is None:
    Calc.calc_annuity(a, b, i)
elif args.type == "annuity" and a is not None:
    Calc.length(a, d, i)
else:
    Calc.calc_prn(d, b, i)

if __name__ == '__main__':
    main()

# print(loan_principal)
# print(first_month)
# print(second_month)
# print(third_month)
# print(final_output)
