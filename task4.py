from datetime import datetime as dt, timedelta as td

users = [
    {"name": "John Doe", "birthday": "1985.03.09"},
    {"name": "Jane Smith", "birthday": "1990.03.16"},
    {"name": "Andrew Backer", "birthday": "1995.06.25"},
    {"name": "Jane Doe", "birthday": "1990.02.10"}
]

def get_upcoming_birthdays(users: list) -> list:
    try:
        birthday_people = []
        current_day = dt.today().date()
        for user in users:
            user_birthday = dt.strptime(user["birthday"], "%Y.%m.%d").date()
            next_congratulations = user_birthday.replace(year=current_day.year)
            difference = (next_congratulations - current_day).days
            if difference < 0:
                next_congratulations = user_birthday.replace(year=current_day.year + 1)
                difference = (next_congratulations - current_day).days

            next_congratulations_weekday = next_congratulations.weekday()

            if 0 <= difference <= 7:
                if next_congratulations_weekday == 6: next_congratulations += td(days=1)
                elif next_congratulations_weekday == 5: next_congratulations += td(days=2)
                congratulations_date = dt.strftime(next_congratulations, "%Y.%m.%d")
                birthday_people.append({"name": user["name"], "congratulation_date": congratulations_date})
        return birthday_people
    except Exception as e:
        print('Function argument must be user list.')
        return []


upcoming_birthdays = get_upcoming_birthdays('safjasf')
print("Список привітань на цьому тижні:", upcoming_birthdays)