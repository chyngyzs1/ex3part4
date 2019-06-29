class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
        self.fuel = 70
        
    def drive(self, distance):
        if distance < self.fuel * 10:
            print('\nLet’sdrive!')
            Car.__add_distance(self, distance)
            Car.__subtract_fuel(self, distance)
        else:
            print('\nNeed more fuel, please, fill more!')
    
    def __add_distance(self, distance):
        self.odometer += distance
        print('Car distance is: ', self.odometer, 'km/h')
    
    def __subtract_fuel(self, distance):
        self.fuel = self.fuel - (distance / 10)
        print('Remaining fuel: ',self.fuel)

ata = Car('LX570', 'Lexus', 2018)
ata.drive(500)
