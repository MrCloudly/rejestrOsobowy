import Models
import Terminal
import TypeControl

class Add:
    def __init__(self):
        self.name = "add"
        self.description = "Dodaje nowy rekord"

    def __str__(self):
        return f"name: {self.name}, default: {self.description}"
    
    @staticmethod
    def run(guid=None,**newType):
        if newType is not None and guid is not None:
            data = Models.ModelType(guid)
            for _, obj in newType.items():
                Models.ModelType.add(data, obj)
        else:
            data = Models.ModelType()
            toDo = TypeControl.Controller.InitType(typ="*")
            
            for item in toDo:
                Models.ModelType.add(data,item)

        Terminal.TerminalCommand.cache.append(data)

        