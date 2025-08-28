import datetime, Bday_Messages
today = datetime.date.today()
next_birthday = datetime.date(2025,8,28)
days_away = next_birthday - today
if today == next_birthday:
    print(Bday_Messages.random_message)
else:
    print(f'My next birthday is {days_away.days} days away!')
