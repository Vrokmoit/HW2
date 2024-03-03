# console_output.py
from output import OutputInterface


class ConsoleOutput(OutputInterface):

    def display_text(self, text):
        print(text)

    def display_error(self, error):
        print(f"Error: {error}")
