from abc import ABC, abstractmethod


class Importer(ABC):
    @classmethod
    @abstractmethod
    def import_data(cls):
        raise NotImplementedError()

    @staticmethod
    def raise_extension_error(received, expected):
        if received != expected:
            raise ValueError("Arquivo inválido")
