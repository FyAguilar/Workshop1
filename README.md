# Workshop1

## General Description:

This program simulates a vehicle catalog. It allows you to create engines, cars, trucks, yachts and motorcycles. It also allows you to view the list of created engines and the complete list of vehicles in the catalog.

## Classes:

**Engine:** This class represents the engine of a vehicle. It has attributes for fuel type (***type_***), horsepower (***potency***) and weight (***weight***). It also has a get_information method that returns a dictionary with the engine information.

**Vehicle:** This is an abstract class that represents a generic vehicle. It inherits from the Engine class and includes attributes for chassis (***chassis***), model (***model***), year (***year***) and engine (***engine***). It also has an abstract calculate_consumption method that is implemented in the child classes to calculate consumption.

**Car, Truck, Yacht, Motorcycle:** These classes inherit from the Vehicle class and implement the specific functionality of each type of vehicle. The information method of these classes calculates the vehicle's consumption using the inherited calculate_consumption method and returns a dictionary with the vehicle's information.

## Functions:

**principal_menu:** This function displays the main menu on the screen and interacts with the user to obtain the selected option.

**create_engine:** This function creates a new engine by requesting user data (type, power and weight) and adds it to the engines dictionary.

**create_vehicle:** This function creates a new vehicle based on the option chosen by the user (car, truck, yacht or motorcycle). It requests the vehicle data (chassis, engine, year and model) and adds it to the corresponding dictionary within the vehicles dictionary.

**run:** This function is the entry point of the program. It starts a loop that shows the main menu and executes the corresponding functions depending on the option chosen by the user.

## Dictionaries:

**engines:** This dictionary stores the information of the created engines. The key is the engine name and the value is the dictionary with the information obtained from the get_information method of the Engine class.

**vehicles:** This dictionary stores the information of the created vehicles. Each key of the main dictionary represents a type of vehicle (Cars, Trucks, Yachts, Motorcycles) and the associated value is another dictionary where the key is the vehicle model and the value is the dictionary with the information obtained from the information method of the corresponding class (Car, Truck, Yacht or Motorcycle).
