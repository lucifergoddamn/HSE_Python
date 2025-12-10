from datetime import datetime, timedelta
def date_range(start_date, end_date):
    try:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        if start > end:
            return []
        days_count = (end - start).days + 1
        result = []
        for i in range(days_count):
            current_date = start + timedelta(days=i)
            result.append(current_date.strftime("%Y-%m-%d"))
        return result
    except ValueError:
        return []
print(date_range('2022-01-01', '2022-01-03'))