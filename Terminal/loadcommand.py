import Terminal
import TypeControl

class Load:
    def __init__(self):
        self.name = "load"
        self.description = "Importuje plik znajdujacy się w katalogu Import (należy wskazać nazwę w formularzu)"

    def __str__(self):
        return f"name: {self.name}, default: {self.description}"
    
    @staticmethod
    def run():
        name = input("Podaj nazwe pliku znajdujacego się w katalogu Import: ")
        with open(f"Import/{name}", "r", encoding="utf-8") as file:
            importData = file.read()

        records = importData.split(";")
        for record in records:
            lines = [line for line in record.split("\n") if line.strip()]
            if "Guid" in lines[0]:
                header = lines.pop(0)
                _, guid = header.split(": ")
                newTypes = {}
                for line in lines:
                    obj, data = line.split(" - ")
                    config = {}
                    attributes = [item.strip().split(": ") for item in data.split(", ")]
                    for attr_name, attr_value in attributes:
                        config.update({attr_name: attr_value})
                    
                    objectInstance = TypeControl.Controller.InitType(typ=obj.strip(), **config)
                    newTypes[obj.strip()] = objectInstance
                
                Terminal.Add.run(guid,**newTypes)
            else:
                print("Nieznaleziono headera Guid")