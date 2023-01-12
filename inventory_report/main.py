from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
import sys


importers = {"csv": CsvImporter, "json": JsonImporter, "xml": XmlImporter}


def main():

    if len(sys.argv) < 3:
        print("Verifique os argumentos", file=sys.stderr)
        return

    [current_file, file_path, report_type] = sys.argv

    importer = importers[file_path.split(".")[1]]
    inventory = InventoryRefactor(importer)
    report = inventory.import_data(file_path, report_type)
    print(report, end="")
