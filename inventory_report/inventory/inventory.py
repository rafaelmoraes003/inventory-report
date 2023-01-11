from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


reports = {"simples": SimpleReport, "completo": CompleteReport}

actions_by_file_extension = {
    "csv": lambda path: CsvImporter(path),
    "json": lambda path: JsonImporter(path),
    "xml": lambda path: XmlImporter(path),
}


class Inventory:
    @staticmethod
    def read_data(file_path):
        extension = file_path.split(".")[1]
        data = actions_by_file_extension[extension](file_path)
        return data

    @classmethod
    def import_data(cls, file_path, report_type):
        products_list = cls.read_data(file_path)
        products_report = reports[report_type].generate(products_list)
        return products_report
