#user story: list out anyone who were born within the last 30 days.
import datetime

def born_within30(date_now,date_birth,name):
    if abs((date_now - date_birth)).days <30:
        print(f"{name} were born within {abs((date_now - date_birth)).days} days")
        return f"{name} were born within {abs((date_now - date_birth)).days} days"

def list_born_within30(indi):
    date_now = datetime.now()
    for a in indi.values():
        dt_birth = datetime.strptime(a.Birthday, '%d %b %Y')
        born_within30(date_now,dt_birth,a.Name)