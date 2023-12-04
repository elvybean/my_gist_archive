import dc1m
current_month = int(input("what is the current month (as an int)"))
curent_year = int(input("what is the current year"))
current_issue = int(input("what is the current issue of dectective comics"))
months_left = (1000000 - current_issue) / 2

future_date = dc1m.months_left(current_month, curent_year, months_left)

print("And the Month will be", future_date[0])
print("The Year will be", future_date[1])

"""
When entering 5, 2022 and 1060 respectively the output is still the same
Output:
The Year will be 43644.0
And the Month will be 11.0
"""