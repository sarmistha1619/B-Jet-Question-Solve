class Toll_booth:
    def __init__(self,motorcycle, Bus, Truck, Car, Train):
        self.motorcycle = motorcycle
        self.Bus = Bus
        self.Truck = Truck
        self.Car = Car
        self.Train = Train
    def weight_of_vehicle(self,weight):
        self.weight = weight

class Taxpayer(Toll_booth):
    def card(self,Platinum, Gold, Silver):
        self.Platinum=Platinum
        self.Gold=Gold
        self.Silver=Silver

    def platinum(self):
        print("10% discount")
    def gold(self):
        print("8% discount")
    def silver(self):
        print("5% discount")


class Govt(Toll_booth):
    def __init__(self):
        pass

class Personal(Toll_booth):
    def __init__(self):
        pass
    def govt_official(self):
        print("2% discount")

class Carriage_of_good(Toll_booth,Taxpayer):
    def __init__(self):
        pass

class Public(Toll_booth,Taxpayer):
    def __init__(self):
        pass

govt_vehicle = Govt()
personal_vehicle = Personal()
carriageGood_vehicle = Carriage_of_good()
public_vehicle= Public()

