from _datetime import datetime

def get_days_from_today(date: str) -> int:
    try:
        #cast date into datetime object
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
        #get todays date
        today_date = datetime.today().date()
        #count date difference
        difference = today_date - given_date
        return difference.days
    except ValueError:
        raise ValueError("Неправильний формат дати. Використовуйте 'YYYY-MM-DD'.")


print(get_days_from_today("1981-10-09"))
