import Terminal

class Save:
    def __init__(self):
        self.name = "save"
        self.description = "Eksportuje cache do pliku"

    def __str__(self):
        return f"name: {self.name}, default: {self.description}"
    
    @staticmethod
    def run():
        name = input("Pod jaka nazwa chcesz zapisac plik: ")
        with open(f"Import/{name}","w",encoding="utf-8") as file:
        
            for index, data_object in enumerate(Terminal.TerminalCommand.cache):
                attributes = vars(data_object)
                for attr_name, attr_value in attributes.items():
                    if hasattr(attr_value, '__dict__'):
                        sub_attributes = vars(attr_value)
                        formatted_sub_attributes = ", ".join([f"{key}: {value}" for key, value in sub_attributes.items()])
                        file.write(f"{attr_name.capitalize()} - {formatted_sub_attributes}\n")

                    else:
                        file.write(f"{attr_name.capitalize()}: {attr_value}\n")
                if index != len(Terminal.TerminalCommand.cache) - 1:
                    file.write(";\n")

            file.close()