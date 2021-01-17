""" Calculate HRA: permissible deduction """


def permissible_hra(basic, hra, rent, period):
    """
    param basic: monthly basic salary
    param hra: hra component in the salary
    param rent: actual rent per month
    param period: numbers of months employed
    returns permissible hra amount
    """
    actual_rent = rent * period
    ten_percent_of_basic = basic * period * 0.1
    rent_paid_minus_basic = actual_rent - ten_percent_of_basic
    fifty_percent_basic = basic * period * 0.5
    hra_received = hra * period
    return min(rent_paid_minus_basic, fifty_percent_basic, hra_received)


def income_tax(income):
    """
    param income: taxable income
    returns tax
    """
    above_two_and_half = 250000 * 0.05
    above_five = 500000 * 0.2
    if income > 1000000:
        tax = (income - 1000000) * 0.3 + above_two_and_half + above_five
    elif 500000 < income < 1000001:
        tax = (income - 500000) * 0.2 + above_two_and_half
    elif 250000 < income < 500001:
        tax = (income - 250000) * 0.05
    else:
        tax = 0

    return tax
