import Terminal

# klasa TerminalCommand uruchamia terminal, przechowuje cache sesji terminala oraz umożliwia wywoływanie menu wyboru
class TerminalCommand:

    cache = []

    @staticmethod
    def select():
        counter = 0
        if len(Terminal.TerminalCommand.cache) != 0:
            output = {}
            for data_object in Terminal.TerminalCommand.cache:
                attr = vars(data_object)
                counter = counter + 1
                output.update({counter: attr['guid']})
                print(f"{counter}. GUID: {attr['guid']}")

            response = int(input("Wybierz rekord: "))
            return output[response]
        print("W rejestrze nie ma danych! Dodaj lub zaimportuj.")
        return None

    @staticmethod
    def run():

        TerminalCommand.cache = []

        while True:
            response = str(input(">"))

            Command = getattr(Terminal, response.capitalize(),None)
            if Command and hasattr(Command, "run"):
                Command.run()
            else:
                print("Nie ma takiego polecenia! Użyj komendy help aby zobaczyć listę dostępnych komend.")