# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 11:01:48 2020

@author: simiyu
"""

import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
from decimal import Decimal


def getPeriodicRepayment(principal, rate, period):
    percrate = rate/1200
    numereta = percrate*((percrate+1)**(period))
    denomineta = ((percrate+1)**(period))-1
    numden = numereta/denomineta
    return round((principal*numden),2)

def getInterestOnRemainingBalance(principal, rate):
    percrate = rate/1200
    return round((percrate*principal),2)

def getNextRepaymentDate(startDate):
    return startDate+ relativedelta(months=1)


def amortizationReducingBalance(amt, rate, periods):
    data = pd.DataFrame()
    scheduledPay = getPeriodicRepayment(amt, rate, periods)
    monthlyIntr = getInterestOnRemainingBalance(amt, rate)
    monthlyprincipal = scheduledPay-monthlyIntr
    closing = amt-monthlyprincipal

    paydate = datetime.today()

    data = data.append({'Date' : paydate.strftime('%d/%m/%Y') , 'Opening Balance' : amt, 'Scheduled Payment' : scheduledPay, 'Monthly Principal' : monthlyprincipal, 'Monthly Interest' : monthlyIntr, 'Closing Balance' : closing} , ignore_index=True)

    commulativeIntr = monthlyIntr;
    x = 0
    while x < periods-1:
        paydate = getNextRepaymentDate(paydate);
        closing = amt-monthlyprincipal
        amt = closing;

        monthlyIntr = getInterestOnRemainingBalance(amt, rate)
        commulativeIntr = commulativeIntr+monthlyIntr
        monthlyprincipal = scheduledPay-monthlyIntr
        closing = closing-monthlyprincipal

        if scheduledPay >amt:
            scheduledPay = amt
            monthlyprincipal = scheduledPay-monthlyIntr

        if closing < 0:
            closing = 0

        data = data.append({'Date' : paydate.strftime('%d/%m/%Y') , 'Opening Balance' : amt, 'Scheduled Payment' : scheduledPay, 'Monthly Principal' : monthlyprincipal, 'Monthly Interest' : monthlyIntr, 'Closing Balance' : closing} , ignore_index=True)
        x = x+1

    return data


def main():
    print('================ This a monthly Schedule (First payment date is a month from today)===========================================')
    amt = float(input("Enter Loan Amount (eg 1000000) : "))
    rate = float(input("Enter Anual interest rate(without % eg 12)  : "))
    periods = int(input("Enter number of months the loan is to be repaid (eg 48) : "))
    choice = str(input("Enter 'E' to export to Excel or anything to print on terminal : "))
    if choice == 'E':
        amortizationReducingBalance(amt, rate, periods).to_excel('amortization.xlsx')
    else:
        print(amortizationReducingBalance(amt, rate, periods))


if __name__ == '__main__':
    main()
