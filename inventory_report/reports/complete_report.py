from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def get_companies_occurrences(products_list: list[dict]):
        products_by_company = {}

        for product in products_list:
            if product["nome_da_empresa"] in products_by_company:
                products_by_company[product["nome_da_empresa"]] += 1
            else:
                products_by_company[product["nome_da_empresa"]] = 1

        return products_by_company

    @staticmethod
    def format_companies_ocurrencies(companies: dict):
        final_str = ""

        for key in companies:
            final_str += f"- {key}: {companies[key]}\n"

        return final_str

    @staticmethod
    def generate(products_list: list[dict]):
        [manufacturing_dates, expiration_dates] = CompleteReport.get_dates(
            products_list
        )
        nearest_expiration_date = CompleteReport.nearest_date_from_today(
            expiration_dates
        )
        most_common_company = CompleteReport.get_most_common_company(
            products_list
        )
        companies_occurrences = CompleteReport.get_companies_occurrences(
            products_list
        )

        formated_companies_occurrences = (
            CompleteReport.format_companies_ocurrencies(companies_occurrences)
        )

        return (
            f"Data de fabricação mais antiga: {min(manufacturing_dates)}\n"
            f"Data de validade mais próxima: {nearest_expiration_date}\n"
            f"Empresa com mais produtos: {most_common_company}\n"
            "Produtos estocados por empresa:\n"
            f"{formated_companies_occurrences}"
        )
