import datetime

class Student:
    def __init__(self,firstName=None,lastName=None,birthDate=None):
        if firstName is not None:
            self.firstName = firstName
        else:
            self.firstName = self.prompt_firstName()

        if lastName is not None:
            self.lastName = lastName
        else:
            self.lastName = self.prompt_lastName()

        if birthDate is not None:
            self.birthDate = birthDate
        else:
            self.birthDate = self.prompt_birthDate()

    @staticmethod
    def prompt_firstName():
        return str(input("Podaj imie studenta: "))

    @staticmethod
    def prompt_lastName():
        return str(input("Podaj nazwisko studenta: "))
    
    @staticmethod
    def prompt_birthDate():
        response = str(input("Podaj date urodzenia studenta: "))
        try:
            formattedDate = datetime.date.fromisoformat(response)
            return formattedDate
        except ValueError:
            print("Nieprawidlowy format daty - spróbuj YYYY-MM-DD")
            return Student.prompt_birthDate()

    def __str__(self):
        return f"firstName: {self.firstName}, lastName: {self.lastName}, birthDate: {self.birthDate}"
    