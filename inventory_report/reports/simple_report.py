from datetime import datetime
from collections import Counter


class SimpleReport:
    @staticmethod
    def nearest_date_from_today(dates):
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

    @staticmethod
    def get_dates(products_list):
        manufacturing_dates, expiration_dates = [], []

        for product in products_list:
            manufacturing_dates.append(product["data_de_fabricacao"])
            expiration_dates.append(product["data_de_validade"])

        return [manufacturing_dates, expiration_dates]

    @staticmethod
    def get_most_common_company(products_list):
        companies = [product["nome_da_empresa"] for product in products_list]

        most_common_company = Counter(companies).most_common()[0][0]
        return most_common_company

    @staticmethod
    def generate(products_list):
        [manufacturing_dates, expiration_dates] = SimpleReport.get_dates(
            products_list
        )
        nearest_expiration_date = SimpleReport.nearest_date_from_today(
            expiration_dates
        )
        most_common_company = SimpleReport.get_most_common_company(
            products_list
        )

        return (
            f"Data de fabricação mais antiga: {min(manufacturing_dates)}\n"
            f"Data de validade mais próxima: {nearest_expiration_date}\n"
            f"Empresa com mais produtos: {most_common_company}"
        )
