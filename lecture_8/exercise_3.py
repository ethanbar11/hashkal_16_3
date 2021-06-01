class Car:
    def __init__(self, id, color):
        self.id = id
        self.color = color


class Truck:
    def __init__(self, id, color):
        self.id = id
        self.color = color


class Road6:
    def __init__(self):
        self.vehicles = {}

    def add_vehicle(self, vehicle):
        self.vehicles[vehicle.id] = vehicle

    def remove_vehicle(self, id):
        del self.vehicles[id]

    def print_vehicles(self):
        for key, val in self.vehicles.items():
            print('The vehicle id is : {} of type {} and color {} '.format(val.id, type(val), val.color))


# Creating new instance of road 6 to manage it.
road6 = Road6()

# I want it to run forever.
while True:
    should_add = int(input('Please enter 1 to add vehicle, 2 to remove: '))
    id = int(input('Please enter vehicle ID: '))
    if should_add == 1:
        color = input('Please enter vehicle color: ')
        is_truck = int(input('Please enter 1 to add a truck, 2 for car: '))
        # None in python is empty, meaning vehicle is now an empty object.
        vehicle = None
        if is_truck == 1:
            vehicle = Truck(id, color)
        elif is_truck == 2:
            vehicle = Car(id, color)
        road6.add_vehicle(vehicle)
    elif should_add == 2:
        road6.remove_vehicle(id)
    road6.print_vehicles()

# truck1 = Truck(123, 'color')
# truck2 = Truck(4, 'fff')
# truck3 = truck1 + truck2
