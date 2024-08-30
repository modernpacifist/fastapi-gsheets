import os
import docx

from abc import ABC, abstractmethod


class DocxBuilder(ABC):
    def __init__(self):
        self.path = './docx_files_storage'

    def save_doc(self, doc, name):
        try:
            if not os.path.exists(self.path):
                os.makedirs(self.path)

            path = f'{self.path}/{name}'
            doc.save(path)
            return path

        except Exception as e:
            print(f'Warning: could not create directory for docx files {e}')

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
    def create(self, data, name):
        doc = docx.Document()

        for d in data:
            doc.

        return self.save_doc(doc, name)


class PublicationsReport(DocxBuilder):
    pass
