import docx
from abc import ABC, abstractmethod
# import abc


class DocxBuilder(ABC):
    @abstractmethod
    def define_steps(self):
        pass

    @abstractmethod
    def generate(self):
        pass

    @abstractmethod
    def save(self):
        pass


class ApplicationsReport(DocxBuilder):
    pass


class ConferenceReport(DocxBuilder):
    pass


class PublicationsReport(DocxBuilder):
    pass
