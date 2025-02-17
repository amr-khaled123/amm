#===================================
#==Oractical Your Age Full Details==
#===================================

#Input Age
age=float(input("What's your age?"))

#Get age in All time units
months=age*12
weeks=months*4
days=age*365.25
hours=days*24
minutes=hours*60
second=minutes*60
birth=2023-age
#Age=
print(f"your months {months}")
print(f"your weeks {weeks}")
print(f"your days{days:f}")
print(f"your hours {hours:f}")
print(f"{minutes:f} minutes")
print(f"{second:f} second")
print(f"{birth:.0f}s")