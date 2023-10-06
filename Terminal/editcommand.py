import Terminal
import TypeControl

class Edit:
    def __init__(self):
        self.name = "edit"
        self.description = "Edytuje rekord po wskazaniu guid oraz danych do zmiany"

    def __str__(self):
        return f"name: {self.name}, default: {self.description}"
    
    @staticmethod
    def prompt():

        counter = 0
        output={}
        if len(TypeControl.Controller.get_types()) != 0:
            for typ in TypeControl.Controller.get_types():
                counter = counter + 1
                output.update({counter: typ})
                print(f"{counter}. {typ}")

            response = int(input("Wybierz typ: "))
            return output[response]
        print("Brak modeli typów w Models!")
        return 0

    @staticmethod
    def run(guid=None,typ=None):
        if guid is None:
            guid = Terminal.TerminalCommand.select()
        if typ is None:
            typ = Edit.prompt()
        if typ == 0:
            return

        for data_object in Terminal.TerminalCommand.cache:
            if getattr(data_object, "guid", None) == guid:
                if hasattr(data_object, typ.lower()):
                    target_object = getattr(data_object, typ.lower())
                    attributes = vars(target_object)
                    for attr_name, _ in attributes.items():
                        new_value = input(f"Podaj nową wartość dla {typ} -> {attr_name} (obecnie {attributes[attr_name]}): ")
                        if new_value:
                            setattr(target_object, attr_name, new_value)
                    print(f"Obiekt o guid {guid} został zedytowany.")
                    return
            else:
                print(f"Nie znaleziono obiektu o guid {guid}.") 