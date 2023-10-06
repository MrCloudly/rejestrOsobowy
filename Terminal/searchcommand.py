import Terminal

class Search:
    def __init__(self):
        self.name = "search"
        self.description = "Przeszukuje cache pod wskazaną frazą"

    def __str__(self):
        return f"name: {self.name}, default: {self.description}"
    
    @staticmethod
    def prompt():
        response = input("Podaj fraze po której chcesz przeszukiwać rejestr: ")
        return response
    
    @staticmethod
    def run(data=None):
        if data is None:
            data = Search.prompt()
        
        matching_objects = []

        for data_object in Terminal.TerminalCommand.cache:
            attributes = vars(data_object)
            for _, attr_value in attributes.items():
                # Sprawdzanie czy atrybut jest prostą wartością (np. string, int)
                if isinstance(attr_value, (str, int, float)) and data in str(attr_value):
                    matching_objects.append(data_object)
                    break
                # Sprawdzanie czy atrybut jest innym obiektem z atrybutami do przeszukania
                if hasattr(attr_value, '__dict__'):
                    sub_attributes = vars(attr_value)
                    if any(data in str(sub_val) for sub_val in sub_attributes.values()):
                        matching_objects.append(data_object)
                        break
        
        if len(matching_objects) != 0:
            Terminal.List.run(matching_objects)
        else:
            print("Nie znaleziono rekordów odpowiadających podanej frazie!")
