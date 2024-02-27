from datetime import date

age_int = 27
name_str = "Spencer"

today_date = date.today()

year_of_birth = today_date.year - age_int

print(f"OMG {name_str}, you are {age_int} years old so you were born in {year_of_birth}")
