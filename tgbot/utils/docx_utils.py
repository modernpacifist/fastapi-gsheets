import docx
from abc import ABC, abstractmethod
# import abc


class DocxBuilder(ABC):
    @abstractmethod
    def generate():
        pass

    @abstractmethod
    def save(self, path):
        pass


class ReportBuilder(DocxBuilder):
    pass


class ConferencesBuilder(DocxBuilder):
    pass


class A(DocxBuilder):
    pass
