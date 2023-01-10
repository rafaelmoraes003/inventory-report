from datetime import datetime
from collections import Counter


class SimpleReport:
    @staticmethod
    def nearest_date_from_today(dates: list[str]):
        dates_from_today = []

        for date in dates:
            [year, month, day] = date.split("-")
            today = datetime.now()
            curr_date = datetime(int(year), int(month), int(day))
            date_diff = (curr_date - today).days
            if date_diff >= 0:
                dates_from_today.append(
                    datetime.strftime(curr_date, "%Y-%m-%d")
                )

        return min(dates_from_today)

