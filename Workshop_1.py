"""
This program consists of a small catalog of vehicles

Autor: Fabian Yesith Aguilar Jimenez
Date: Mar13 - 2024

"""


class Engine:
    """
    This class represents the engine of a vehicle
    """

    def __init__(self, type_: str, potency: float, weight: int):
        self.type = type_
        self.potency = potency
        self.weight = weight

    def get_information(self):
        return {"Type": self.type, "Potency": self.potency, "Weight": self.weight}


class Vehicle(Engine):
    """
    This class represents an abstract class for vehicles
    """

    def __init__(self, chassis: str, model: str, year: int, engine):
        self.chassis = chassis
        self.model = model
        self.year = year
        self.engine = engine
        self.potency = engines[f"{engine}"]["Potency"]
        self.weight = engines[f"{engine}"]["Weight"]

    def calculate_consumption(self):
        return (
            (1.1 * self.potency)
            + (0.2 * self.weight)
            - (0.3 if self.chassis == "A" else 0.5)
        )


class Car(Vehicle):
    """This class represent a concreted implementation of the Vehicle class."""

    def information(self):
        self.consumption = Vehicle.calculate_consumption(self)
        return {
            "Chassis": self.chassis,
            "Model": self.model,
            "Year": self.year,
            "Consumption": self.consumption,
        }


class Truck(Vehicle):
    """This class represent a concreted implementation of the Vehicle class."""

    def information(self):
        self.consumption = Vehicle.calculate_consumption(self)
        return {
            "Chassis": self.chassis,
            "Model": self.model,
            "Year": self.year,
            "Consumption": self.consumption,
        }


class Yacht(Vehicle):
    """This class represent a concreted implementation of the Vehicle class."""

    def information(self):
        self.consumption = Vehicle.calculate_consumption(self)
        return {
            "Chassis": self.chassis,
            "Model": self.model,
            "Year": self.year,
            "Consumption": self.consumption,
        }


class Motorcycle(Vehicle):
    """This class represent a concreted implementation of the Vehicle class."""

    def information(self):
        self.consumption = Vehicle.calculate_consumption(self)
        return {
            "Chassis": self.chassis,
            "Model": self.model,
            "Year": self.year,
            "Consumption": self.consumption,
        }


def principal_menu():
    """
    This function displays the main menu on the screen
    """
    message = """
    Choose an option:
    1. Create a engine
    2. Create a car
    3. Create a truck
    4. Create a yatch
    5. Create a motorcycle
    6. Show  all engines
    7. Show all vehicles
    8. Exit
    """
    print(message)
    global option
    option = int(input())


def create_engine():
    """
    This function creates a new engine and adds it to an engine dictionary

    Parameters:
    - name (str) : Name to identify the engine
    - type (str) : Type of fuel that the engine uses
    - potency (float) : Potency of the engine
    - weight (float) : weight of the engine

    """

    name = input("Enter the name: ")
    type_ = input("Enter the type: ")
    potency = float(input("Enter the power of the engine: "))
    weight = float(input("Enter the weight: "))
    new_engine = Engine(type_, potency, weight).get_information()
    engines.update({name: new_engine})


def create_vehicle():
    """
    This function creates a new vehicle depending on the user´s choice, and adds it on the corresponding section in the dictionary

    Parameters:
    chassis (str) : Type of chasis for the vehicle
    engine (str) : name of the vehicle's engine, this must be in the engines dictionary
    year (int) : The production year of the vehicle
    model (str): The model of the vehicle, this will be the identifier within the dictionary

    """

    chassis = input("Choose the chasis [A/B]: ")
    engine = input(f"Choose an engine: \n {engines} \n :")
    year = int(input("Enter the year: "))
    model = input("Enter the model: ")
    if option == 2:
        new_car = Car(chassis, model, year, engine).information()
        vehicles["Cars"].update({model: new_car})
    if option == 3:
        new_truck = Truck(chassis, model, year, engine).information()
        vehicles["Trucks"].update({model: new_truck})
    if option == 4:
        new_yacht = Yacht(chassis, model, year, engine).information()
        vehicles["Yachts"].update({model: new_yacht})
    if option == 5:
        new_motorcycle = Motorcycle(chassis, model, year, engine).information()
        vehicles["Motorcycles"].update({model: new_motorcycle})


def run():
    """
    This  function is used to start the program and display the main menu options.
    It uses a while loop that continues until the user chooses to exit the program.
    """

    principal_menu()
    while option != 8:
        if option == 1:
            create_engine()

        elif option in [2, 3, 4, 5]:
            create_vehicle()

        elif option == 6:
            print(engines)

        elif option == 7:
            print(vehicles)

        else:
            raise ValueError("Invalid Option")
        principal_menu()


vehicles = {"Cars": {}, "Trucks": {}, "Yachts": {}, "Motorcycles: ": {}}
engines = {}

if __name__ == "__main__":
    run()
