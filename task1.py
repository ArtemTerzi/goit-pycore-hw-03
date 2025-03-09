from datetime import datetime as dt

def get_days_from_today(date: str) -> int:
    try:
        return (dt.today().date() - dt.strptime(date, '%Y-%m-%d').date()).days
    except Exception:
        print('Invalid date format. Please use YYYY-MM-DD format.')