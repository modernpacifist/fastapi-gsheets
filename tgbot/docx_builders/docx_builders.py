import docx
from abc import ABC, abstractmethod


class DocxBuilder(ABC):
    def __init__(self, filename, data):
        self.path = './docx_files_storage'

    # @abstractmethod
    # def create(self):
    #     raise NotImplementedError('Method not implemented')

    def save(self, doc):
        doc.save(f'{self.path}/{self.filename}')


class ApplicationsReport(DocxBuilder):
    def create(self, data):
        def distribute_data(data):
            return data[0]

        data = distribute_data(data)

        self.doc = docx.Document()
        self.doc.add_heading(data, 0)
        self.doc.save(data)

    def save(self, path='.'):
        try:
            self.doc.save(f'{path}/{self.filename}')

        except Exception as e:
            print(e)


class ConferenceReport(DocxBuilder):
    @staticmethod
    def create(self, data):



class PublicationsReport(DocxBuilder):
    pass
