from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, file_path):

        extension = file_path.split(".")[1]
        cls.raise_extension_error(extension, "json")

        with open(file_path, mode="r") as file:
            content = json.load(file)
        return content
