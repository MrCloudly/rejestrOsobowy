import Terminal

class Remove:
    def __init__(self):
        self.name = "remove"
        self.description = "Usuwa rekord"

    def __str__(self):
        return f"name: {self.name}, default: {self.description}"
    
    @staticmethod
    def run(guid=None):
        if guid is None:
            guid = Terminal.TerminalCommand.select()
            
        for index, data_object in enumerate(Terminal.TerminalCommand.cache):
            if getattr(data_object, "guid", None) == guid:
                del Terminal.TerminalCommand.cache[index]
                print(f"Obiekt o guid {guid} został usunięty.")
                return
        print(f"Nie znaleziono obiektu o guid {guid}.") 
            