class Soldier:
    def __init__(self, last_name, first_name, company, platoon):
        self.last_name = last_name
        self.first_name = first_name
        self.name = f'{self.last_name}, {self.first_name}'

        self.company = company
        self.platoon = platoon

    def __str__(self):
        return f'{self.name} - {self.company}/{self.platoon}PLT'