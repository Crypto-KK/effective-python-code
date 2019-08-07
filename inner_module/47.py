from decimal import Decimal, ROUND_UP, ROUND_DOWN

rate = Decimal('1.45')
seconds = Decimal('222')
cost = rate * seconds / Decimal('60')
print(cost)

rounded = cost.quantize(Decimal('0.01'), rounding=ROUND_UP)
print(rounded)

print('==========')


cost = Decimal('0.05') * Decimal('5') / Decimal('60')
print(cost)
rounded = cost.quantize(Decimal('0.01'), rounding=ROUND_UP)
print(rounded)
