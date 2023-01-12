from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport
from pytest import fixture


@fixture
def product_data():
    return [
        {
            "id": 1,
            "nome_do_produto": "Cafe",
            "nome_da_empresa": "Cafes Nature",
            "data_de_fabricacao": "2020-07-04",
            "data_de_validade": "2023-02-09",
            "numero_de_serie": "FR48",
            "instrucoes_de_armazenamento": "instrucao",
        }
    ]


def test_decorar_relatorio(product_data):
    RED = "\033[31m"
    GREEN = "\033[32m"
    BLUE = "\033[36m"

    colored_report = ColoredReport(SimpleReport)
    colored_text = colored_report.generate(product_data).split("\n")

    titles = []
    dates = []

    for line in colored_text:
        titles.append(line.split(":")[0])
        dates.append(line.split(":")[1])
        company = line.split(":")[1]
    dates.pop()

    for title in titles:
        assert (GREEN in title) is True

    for date in dates:
        assert (BLUE in date) is True

    assert (RED in company) is True
