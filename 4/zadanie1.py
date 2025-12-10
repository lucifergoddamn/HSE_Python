from datetime import datetime
date_str1 = "Wednesday, October 2, 2002"
dt1 = datetime.strptime(date_str1, "%A, %B %d, %Y")
date_str2 = "Friday, 11.10.13"
dt2 = datetime.strptime(date_str2, "%A, %d.%m.%y")
date_str3 = "Thursday, 18 August 1977"
dt3 = datetime.strptime(date_str3, "%A, %d %B %Y")
print("Газеты:")
print(f"The Moscow Times: {dt1}")
print(f"The Guardian: {dt2}")
print(f"Daily News: {dt3}")