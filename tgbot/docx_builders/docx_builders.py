import docx
from abc import ABC, abstractmethod
# import abc


class DocxBuilder(ABC):
    def __init__(self, filename, path, data):
        self.filename = filename
        self.path = path
        self.data = data
        self.document = docx.Document()

    @abstractmethod
    def generate(self, info):
        print(info)

    def save(self, path):
        pass


class ApplicationsReport(DocxBuilder):
    def __init__(self):
        super().__init__()
        pass


class ConferenceReport(DocxBuilder):
    pass


class PublicationsReport(DocxBuilder):
    pass
