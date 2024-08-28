import docx
from abc import ABC, abstractmethod


class DocxBuilder(ABC):
    def __init__(self, filename, data):
        self.filename = filename
        self.data = data

    @abstractmethod
    def create(self):
        raise NotImplementedError('Method not implemented')

    def save(self, path):
        self.document.save(f'{path}/{self.filename}')


class ApplicationsReport(DocxBuilder):
    def __init__(self, filename, data):
        super().__init__(filename, data)


class ConferenceReport(DocxBuilder):
    pass


class PublicationsReport(DocxBuilder):
    pass
