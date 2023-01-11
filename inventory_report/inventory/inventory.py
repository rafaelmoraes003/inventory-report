from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xmltodict

reports = {"simples": SimpleReport, "completo": CompleteReport}

actions_by_file_extension = {
    "csv": lambda file: list(
        csv.DictReader(file, delimiter=",", quotechar='"')
    ),
    "json": lambda file: json.load(file),
    "xml": lambda file: xmltodict.parse(file.read())["dataset"]["record"],
}


class Inventory:
    @staticmethod
    def read_data(file_path):
        extension = file_path.split(".")[1]
        with open(file_path, mode="r") as file:
            extension = file_path.split(".")[1]
            data = actions_by_file_extension[extension](file)
        return data

    @classmethod
    def import_data(cls, file_path, report_type):
        products_list = cls.read_data(file_path)
        products_report = reports[report_type].generate(products_list)
        return products_report
