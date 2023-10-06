import Terminal

class List:
    def __init__(self):
        self.name = "list"
        self.description = "Wyswietla zapisane dane w cache programu"

    def __str__(self):
        return f"name: {self.name}, default: {self.description}"
    
    @staticmethod
    def run(data=None):
        if data is None: data = Terminal.TerminalCommand.cache
        for data_object in data:
            attributes = vars(data_object)
            for attr_name, attr_value in attributes.items():
                if hasattr(attr_value, '__dict__'):
                    sub_attributes = vars(attr_value)
                    formatted_sub_attributes = ", ".join([f"{key}: {value}" for key, value in sub_attributes.items()])
                    print(f"{attr_name.capitalize()} - {formatted_sub_attributes}")

                else:
                    print(f"{attr_name.capitalize()}: {attr_value}")


        