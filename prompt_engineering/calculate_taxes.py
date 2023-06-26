# Calculate taxes

values = [
    31000,
    15000,
    52000,
    103000,
    42000,
    156000,
    15000,
    27000,
    82000,
    33000,
    25000,
    17000,
    53000,
    35000,
    120000,
    74000,
    28000,
    64000,
    29000,
    14000,
]

total = 0
for salary in values:
    if salary <= 20000:
        total += salary * 0.1  # 10%
        print(salary * 0.1)
    elif salary > 20000 and salary <= 40000:
        total += salary * 0.2  # 20%
        print(salary * 0.2)
    else:
        total += salary * 0.3  # 30%
        print(salary * 0.3)


print("Total tax is", total)


# 6200.0 + 1500.0 + 15600.0 + 30900.0 + 12600.0 + 46800.0 + 1500.0 + 5400.0 + 24600.0 + 6600.0 + 5000.0 + 1700.0 + 15900.0 + 7000.0 + 36000.0 + 22200.0 + 5600.0 + 19200.0 + 5800.0 + 1400.0
# The answer: Total tax is 271500.0
