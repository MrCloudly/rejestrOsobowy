import inspect
import Terminal

class Help:
    def __init__(self):
        self.name = "help"
        self.description = "Wyswietla listę komend wraz z ich opisami"

    def __str__(self):
        return f"name: {self.name}, default: {self.description}"

    @staticmethod
    def commands():
        classes = []
        for _, obj in inspect.getmembers(Terminal):
            if inspect.ismodule(obj):
                for _, class_obj in inspect.getmembers(obj):
                    if inspect.isclass(class_obj):
                        if(class_obj.__name__ != "TerminalCommand"):
                            classes.append(class_obj)
        return classes

    @staticmethod 
    def HelpCommand():
        classes = Help.commands()
        instances = [cls() for cls in classes]
        for instance in instances:
            print(f"Polecenie: {instance.name}, opis: {instance.description}")

    @staticmethod
    def run():
        Help.HelpCommand()
        print("Polecenia nie zawierają argumentów. Jeśli konieczne jest wskazanie dodatkowych opcji uruchomi się formularz.")