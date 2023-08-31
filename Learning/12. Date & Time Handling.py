#Date Time handling in Python
import datetime as dt

print("-------------------------------------------------------------")

#Date
print("Date: \n") 

current_date=dt.date.today()
print("Current Date:",current_date)

#creating a new date

new=dt.date(2023,4,1)
print("Newly Created Date: ",new)

print("\n")
#Acessing Year,Mont and date individually

print("Year: ",new.year)
print("Month: ",new.month)
print("date: ",new.day)

print("-------------------------------------------------------------")

#Time
print("Time: \n")

current_time=dt.datetime.now()
print("Current Time:",current_time)

a=dt.time(10,45,20,343353)
print("Newly Created Time: ",a)

print("\n")

print("Hour: ",a.hour)
print("Minute: ",a.minute)
print("Second: ",a.second)
print("Microsecond: ",a.microsecond)

print("-------------------------------------------------------------")

#Creating a new Datetime module

new=dt.datetime(2023,4,1,7,15,20)
print("Newly Created DateTime:",new)

#Can call the Date & Time individually from the variable("new")

print("Date:",new.date())
print("Time:",new.time())

print("-------------------------------------------------------------")


#Can find number of days left for NewYear

current=dt.datetime.now()
New_Year=dt.datetime(2024,1,1)
difference=New_Year-current

print("Remaining Days Left: ",difference)

print("-------------------------------------------------------------")

current=dt.datetime.now()
print("Current DateTime:",current)

#Custom Formatting tha Date & Time using constructor & Format specifiers

s=current.strftime("%A %B %d %Y")
print(s)

print("-------------------------------------------------------------")

