from babel import Locale
from babel.numbers import format_decimal, format_currency


def investment_value(start, interest_rate, tax_rate, deposit, years):
    balance = start
    for _ in range(1, years + 1):
        interest_earned = balance * interest_rate
        taxes = interest_earned * tax_rate
        balance += (interest_earned - taxes + deposit)
    return balance


def years_to_reach_goal(start, interest_rate, tax_rate, deposit, goal):
    years = 0
    balance = start
    while balance < goal:
        interest_earned = balance * interest_rate
        taxes = interest_earned * tax_rate
        balance += (interest_earned - taxes + deposit)
        years += 1
    return years


print(format_currency(investment_value(
    start=1000, interest_rate=0.05,
    tax_rate=0, deposit=0, years=10), 'PEN', locale='es_PE'))


print(investment_value(start=1000, interest_rate=0.05, 
    tax_rate=0, deposit=0, years=10))  # should be 1628.89
print(investment_value(start=1000, interest_rate=0.05, 
    tax_rate=0, deposit=100, years=10))  # should be 2886.68
print(investment_value(start=10000, interest_rate=0.13,
    tax_rate=0.25, deposit=1000, years=30))  # should be 319883.75
print(investment_value(start=1, interest_rate=1, 
    tax_rate=0, deposit=0, years=20)) # should be 1048576.0

print(years_to_reach_goal(100, 0.05, 0.04, 100, 1200))
print(years_to_reach_goal(300, 0.025, 0.02, 100, 1400))
print(years_to_reach_goal(200, 0.06, 0.03, 150, 1300))
print(years_to_reach_goal(250, 0.04, 0.05, 130, 1600))