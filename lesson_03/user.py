class User:

    def __init__(self, firstName, lastName):
        self.first_name = firstName
        self.last_name = lastName

    def sayFirstName(self):
        print(self.first_name)

    def sayLastName(self):
        print(self.last_name)

    def sayFullName(self):
        print(self.first_name + " " + self.last_name)
