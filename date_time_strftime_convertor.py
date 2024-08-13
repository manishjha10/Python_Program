from datetime import datetime
current_time = datetime.now()
formatted_time = current_time.strftime(" today is %jth day of the  year ")
print(formatted_time)
