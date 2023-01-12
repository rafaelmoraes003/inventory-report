from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.inventory.inventory import reports
from collections.abc import Iterable


class InventoryRefactor(Iterable):
    def __init__(self, importer: Importer):
        self.importer = importer
        self.data = []

    def import_data(self, file_path, report_type):
        self.data.extend(self.importer.import_data(file_path))
        return reports[report_type].generate(self.data)

    def __iter__(self):
        return InventoryIterator(self.data)
