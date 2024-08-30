import os
import docx

from abc import ABC, abstractmethod


class DocxBuilder(ABC):
    def __init__(self):
        self.path = './docx_files_storage'

    def create_path(self):
        try:
            os.makedirs(self.path)
        except Exception as e:
            print(f'Warning: could not create directory for docx files {e}')

    def save_doc(self, doc):
        return None

    @abstractmethod
    def create(self):
        raise NotImplementedError('Method not implemented')


class ApplicationsReport(DocxBuilder):
    def create(self, data):
        def distribute_data(data):
            return data[0]

        data = distribute_data(data)

        self.doc = docx.Document()
        self.doc.add_heading(data, 0)
        self.doc.save(data)


class ConferenceReport(DocxBuilder):
    def create(self, data):
        doc = docx.Document()


        if not os.path.exists(self.path):
            self.create_path()
        doc.save(f'{self.path}/conf1.docx')


class PublicationsReport(DocxBuilder):
    pass
