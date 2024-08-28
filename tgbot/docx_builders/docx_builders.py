import docx
from abc import ABC, abstractmethod
# import abc


class DocxBuilder(ABC):
    def __init__(self, filename, data):
        self.filename = filename
        self.data = data
        self.document = docx.Document()

    @abstractmethod
    def generate(self):
        raise NotImplemented(f'{__class__}.generate is not implemented')

    def save(self, path):
        self.document.save(f'{path}/{self.filename}')


class ApplicationsReport(DocxBuilder):
    def __init__(self):
        super().__init__()
        pass


class ConferenceReport(DocxBuilder):
    pass


class PublicationsReport(DocxBuilder):
    pass
