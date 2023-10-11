# # create a all_car list
# import datetime

# class CarManager:
#     all_cars = []
#     car_makes = ["Tesla", "BMW", "Ford"]
#     car_models = ["Model 3", "Model S", "X1", "X5", "F-150", "Ranger"]
#     car_services = ["Tire change", "Oil change"]
#     total_cars = 0

#     def add_car(make, model, year, mileage, services):
#         car = {}
#         car._id = CarManager.total_cars
#         car.set_make = make
#         car.set_model = model
#         car.set_year = year
#         car.set_mileage = mileage
#         car.set_services = services
#         CarManager.all_cars.append(car)

#     def display_menu():
#         return f"----  WELCOME  ----\n1. Add a car\n2. View all cars\n3. View total number of cars\n4. See a car's details\n5. Service a car\n6. Update mileage\n7. Quit\n"
    
#     def process_user_input(user_input):
#         if user_input == 1:
#             pass
#         else:
#             print("Invalid input")
# class Car:
    
#     def __init__(self):
#         pass

#     def __str__(self):
#         return f"Car lot holds {CarManager.total_cars} vehicles"

#     @property
#     def get_id(self):
#         return self._id
    
    
#     @property
#     def get_make(self):
#         return self._make
    
#     @get_make.setter
#     def set_make(self, make):
#         if make in CarManager.car_makes:
#             self._make = make

    
#     @property
#     def get_model(self):
#         return self._model
    
#     @get_model.setter
#     def set_model(self, model):
#         if model in CarManager.car_models:
#             self._model = model

    
#     @property
#     def get_year(self):
#         return self._year
    
#     @get_year.setter
#     def set_year(self, year):
#         if type(year) == int and year >= 1950 and year <= datetime.date.today().year:
#             self._year = year

    
#     @property
#     def get_mileage(self):
#         return self._mileage
    
#     @get_mileage.setter
#     def set_mileage(self, mileage):
#         if type(mileage) == int and mileage >= 0:
#             self._mileage = mileage

    
#     @property
#     def get_services(self):
#         return self._services
    
#     @get_services.setter
#     def set_services(self, services):
#         if type(services) == list:
#             self._services = services

#     def add_service(self, service):
#         if service in CarManager.car_services:
#             self._services.append(service)




# CarManager.add_car("Ford", "Ranger", 2020, 10000, ["Oil change"])
# print(CarManager)
# # while True:
# #     print(CarManager.display_menu())
# #     user_input = input("Select menu item: ")

class CarManager:
    all_cars = {}
    total_cars = 0
    id_counter = 1

    def __init__(self, id, make, model, year):
        self._id = CarManager.id_counter
        CarManager.id_counter += 1
        self._make = make
        self._model = model
        self._year = year
        self._mileage = 0
        self._services = []

        CarManager.all_cars[self._id] = self 
        CarManager.total_cars += 1

    @property
    def get_id(self):
        return self._id

    @property
    def get_make(self):
        return self._make
    
    @get_make.setter
    def set_make(self, make):
        self._make = make

    @property
    def get_model(self):
        return self._model
    
    @get_model.setter
    def set_model(self, model):
        self._model = model

    @property
    def get_year(self):
        return self._year
    
    @get_year.setter
    def set_year(self, year):
        self._year = year

    @property
    def get_mileage(self):
        return self._mileage
    
    @get_mileage.setter
    def set_mileage(self, mileage):
        if mileage < 0:
            print("Wrong Input")
        else:
            self._mileage = mileage

    @property
    def get_services(self):
        return self._services
    
    @get_services.setter
    def set_services(self, service):
        self._services.append(service)

    def __str__(self):
        return f"""ID: {self.get_id}
Make: {self.get_make}
Model: {self.get_model}
Year: {self.get_year}
Mileage: {self.get_mileage}
Services: {", ".join(self.get_services)}"""

def run_the_manager():
    choice = input("""----  WELCOME  ----
1. Add a car
2. View all cars
3. View total number of cars
4. See a car's details
5. Service a car
6. Update mileage
7. Quit\n""")
    match choice:
        case "1":
            id = max(CarManager.all_cars.keys()) if CarManager.all_cars.keys() else 1
            make = input("Enter car make: ")
            model = input("Enter car model: ")
            year = int(input("Enter manufacturing year: "))
            CarManager(id, make, model, year)
            print("Car added successfully!")
            print(CarManager.all_cars)
            return run_the_manager()
        case "2":
            print("All Cars:")
            for car in CarManager.all_cars.values():
                print(f"{car.get_year} {car.get_make} {car.get_model}")
            return run_the_manager()
        case "3":
            print(f"Total number of cars: {CarManager.total_cars}")
            return run_the_manager()
        case "4":
            id = int(input("What is your cars ID?   "))
            print(CarManager.all_cars.get(id))
            return run_the_manager()
        case "5":
            id = int(input("What is your cars ID?   "))
            car = CarManager.all_cars.get(id)
            service = input("Enter service description: ")
            car.set_services = service
            return run_the_manager()
        case "6":
            id = int(input("What is your cars ID?   "))
            car = CarManager.all_cars.get(id)
            mileage = int(input("Enter new mileage: "))
            car.set_mileage = mileage
            return run_the_manager()
        case "7":
            print("Goodbye")
        case _:
            print("Invalid input")
            return run_the_manager()

run_the_manager()

