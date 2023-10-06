import sys

class Exit:
    def __init__(self):
        self.name = "exit"
        self.description = "Opuszcza program"

    def __str__(self):
        return f"name: {self.name}, default: {self.description}"

    @staticmethod
    def run():
        print("Do zobaczenia!")
        sys.exit(0)