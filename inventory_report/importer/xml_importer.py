from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, file_path):

        extension = file_path.split(".")[1]
        cls.raise_extension_error(extension, "xml")

        with open(file_path, mode="r") as file:
            content = xmltodict.parse(file.read())["dataset"]["record"]
        return content
