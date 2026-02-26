from datetime import datetime, timedelta
now = datetime.now()
future = now + timedelta(days=2)
print(future - now)