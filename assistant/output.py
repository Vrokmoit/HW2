# output.py
from abc import ABC, abstractmethod


class OutputInterface(ABC):

    @abstractmethod
    def display_text(self, text):
        pass

    @abstractmethod
    def display_error(self, error):
        pass
