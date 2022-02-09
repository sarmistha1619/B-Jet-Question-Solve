from abc import ABC, abstractmethod

class Car:
    @abstractmethod
    def changeGear(self):
        pass
    @abstractmethod
    def speedUp(self):
        pass
    @abstractmethod
    def applyBrakes(self):
        pass

class  automatic_car_controlling_system:
    def changing_gear(self, speed):
        self.speed = speed
    def speed_up_rate(self, accelerator):
        self.accelerator = accelerator
    def slow_down_rate(self,brakes):
        self.brakes = brakes

class BMWCar(Car,automatic_car_controlling_system):
    def changeGear(self):
        pass
    def speedUp(self):
        pass
    def applyBrakes(self):
        pass
class FordCar(Car,automatic_car_controlling_system):
    def changeGear(self):
        pass
    def speedUp(self):
        pass
    def applyBrakes(self):
        pass
class GMCCar(Car,automatic_car_controlling_system):
    def changeGear(self):
        pass
    def speedUp(self):
        pass
    def applyBrakes(self):
        pass

class Hummer(GMCCar):
    def changeGear(self):
        pass
    def speedUp(self):
        pass
    def applyBrakes(self):
        pass
    def changing_gear(self, gspeed):
        self.gspeed = gspeed
    def speed_up_rate(self, gaccelerator):
        self.gaccelerator = gaccelerator
    def slow_down_rate(self,brakes):
        self.gbrakes = gbrakes

BMW = BMWCar()
BMW.changeGear()
BMW.speedUp()
BMW.applyBrakes()

Ford = FordCar()
Ford.changeGear()
Ford.speedUp()
Ford.applyBrakes()

GMC = GMCCar()
GMC.changeGear()
GMC.speedUp()
GMC.applyBrakes()
GMC.changing_gear()
GMC.speed_up_rate()
GMC.slow_down_rate()


