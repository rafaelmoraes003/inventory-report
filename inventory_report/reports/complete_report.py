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

