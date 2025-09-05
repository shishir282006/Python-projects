from datetime import date , datetime
today = date.today()
dob_input = input("Enter your date of birth (YYYY-MM-DD): ")
dob = datetime.strptime(dob_input, "%Y-%m-%d").date()
print(dob)
age = [today.year - dob.year , today.month - dob.month , today.day - dob.day]
print(f" you are {age} year old")