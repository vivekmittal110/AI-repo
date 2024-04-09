class Vehicle:
    def __init__(self,seating_capacity):
        self.seating_capacity = seating_capacity

    def get_fair(self):
        return self.seating_capacity * 100


class Bus(Vehicle):
    def __init__(self,seating_capacity):
        super().__init__(seating_capacity)

    def get_fair(self):
        vehicel_fair = super().get_fair()
        maintanence = (super().get_fair() * 0.1)
        return vehicel_fair + maintanence
    
vehicle1 = Vehicle(50)
print("Vehicle fair", vehicle1.get_fair())
bus1 = Bus(50)
print("Bus fair",bus1.get_fair())