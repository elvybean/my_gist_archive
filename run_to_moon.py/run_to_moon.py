moon_distance = 225623 #this is the average distance, the furthest distance is 252088 and the shortest is 225623
years = int(input("Please enter the years you're going to keep this up"))
current_age = int(input("Please enter yur current age"))
years_in_days = years * 365
miles_day = moon_distance / years_in_days
print(miles_day, " miles per day is required to run to the moon before you turn", (current_age + years))