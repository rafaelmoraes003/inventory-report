from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, file_path):

        extension = file_path.split(".")[1]
        cls.raise_extension_error(extension, "csv")

        with open(file_path, mode="r") as file:
            content = csv.DictReader(file, delimiter=",", quotechar='"')
            content_list = list(content)
        return content_list
