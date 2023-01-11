from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def get_companies_occurrences(products_list):
        products_by_company = {}

        for product in products_list:
            if product["nome_da_empresa"] in products_by_company:
                products_by_company[product["nome_da_empresa"]] += 1
            else:
                products_by_company[product["nome_da_empresa"]] = 1

        return products_by_company

    @staticmethod
    def format_companies_ocurrencies(companies):
        final_str = ""

        for key in companies:
            final_str += f"- {key}: {companies[key]}\n"

        return final_str

    @classmethod
    def generate(cls, products_list):
        companies_occurrences = cls.get_companies_occurrences(products_list)
        formated_companies_occurrences = cls.format_companies_ocurrencies(
            companies_occurrences
        )
        return (
            f"{SimpleReport.generate(products_list)}\n"
            "Produtos estocados por empresa:\n"
            f"{formated_companies_occurrences}"
        )
