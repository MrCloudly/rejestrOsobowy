class Address:
    def __init__(self,city=None,street=None,houseNo=None):
        if city is not None:
            self.city = city
        else:
            self.city = self.prompt_city()

        if street is not None:
            self.street = street
        else:
            self.street = self.prompt_street()

        if houseNo is not None:
            self.houseNo = houseNo
        else:
            self.houseNo = self.prompt_houseNo()

    @staticmethod
    def prompt_city():
        return str(input("Podaj miasto: "))

    @staticmethod
    def prompt_street():
        return str(input("Podaj ulice: "))
    
    @staticmethod
    def prompt_houseNo():
        return str(input("Podaj numer domu: "))
    
    def __str__(self):
        return f"City: {self.city}, Street: {self.street}, HouseNo: {self.houseNo}"