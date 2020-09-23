name = input("What is your name? \n")
country = input("Where are you from? \n")
age = int(input("How old are you? \n"))
hourly_wage = int(input("What is your hourly wage? \n"))
satisfied = input("Are you satisfied? (y/n) \n")
satisfied_bool = True if satisfied == "yes" else False
daily_wage = hourly_wage * 8
#print(name + country + str(age) + str(hourly_wage) + satisfied)
print(f"Your name is {name} and you're from {country} and you are {age} years old. You make ${hourly_wage} an hour, which is ${daily_wage} per day. Satisfied? {satisfied_bool}")