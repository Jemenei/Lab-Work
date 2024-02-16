#ex 1
from datetime import datetime, timedelta

x = datetime.now()
five_days_ago = x - timedelta(days=5)

print(five_days_ago) 



#ex 2
from datetime import datetime, timedelta

today = datetime.now()
print(today)

yesterday = today - timedelta(days=1)
print(yesterday)

tomorrow = today + timedelta(days=1)
print(tomorrow)



#ex 3
from datetime import datetime

date = datetime.now()

formatted_datetime = date.strftime("%Y - %m - %d %H:%M:%S")
print(formatted_datetime)

#ex 4
from datetime import datetime

datetime1 = datetime(2023, 5, 12, 10, 30, 0)  
datetime2 = datetime(2023, 5, 15, 12, 45, 0)  

datetime_difference = datetime2 - datetime1

difference_in_seconds = datetime_difference.total_seconds()

print("Difference between the two datetimes in seconds:", difference_in_seconds)

