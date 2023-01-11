from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv


reports = {
    "simples": SimpleReport,
    "completo": CompleteReport
}


class Inventory:
    @staticmethod
    def open_csv(file_path, report_type):
        with open(file_path, mode="r") as file:
            data = csv.DictReader(file, delimiter=',', quotechar='"')
        if report_type == "simples":
            return SimpleReport.generate(data)
        else:
            return CompleteReport.generate(data)

    @classmethod
    def import_data(cls, file_path, report_type):
        # products_list = cls.open_csv(file_path)
        # products_report = reports[report_type].generate(products_list)
        return cls.open_csv(file_path, report_type)
