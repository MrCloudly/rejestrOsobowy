import uuid
import TypeControl

# klasa ModelType sluzy do preparowania rekordów przed dodaniem ich do cache.
# Umożliwia ona zbudowanie nowego rekordu a następnie nadanie mu wstępnych danych poprzez nadanie określonych atrybutów (typów dostępnych w Models).
class ModelType:
    def __init__(self,guid=None):
        if guid is not None:
            self.guid = guid
        else:
            self.guid = uuid.uuid4().hex
    
    #dodaje atrybut do obiektu typu ModelType
    def add(self,obj):
        typeName = obj.__class__.__name__.lower()
        avaiableTypes = [types.lower() for types in TypeControl.Controller.get_types()] 
        if (typeName in avaiableTypes):
            setattr(self,typeName,obj)
            return True
        print(f"Nieobsługiwany typ obiektu: {typeName}")
        return False
    

    # metod remove() i edit() przeniesiona bezposrednio do komend zarzadzajacych cache terminala (nie ma potrzeby edytowania samego obiektu)