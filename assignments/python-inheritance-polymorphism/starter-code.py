class Vehicle:
    def __init__(self, brand: str, max_speed: int):
        self.brand = brand
        self.max_speed = max_speed

    def move(self) -> str:
        raise NotImplementedError("Subclasses must implement move().")


class Car(Vehicle):
    def move(self) -> str:
        return f"{self.brand} car drives on the road at up to {self.max_speed} km/h."


class Bike(Vehicle):
    def move(self) -> str:
        return f"{self.brand} bike pedals along at up to {self.max_speed} km/h."


class Boat(Vehicle):
    def move(self) -> str:
        return f"{self.brand} boat sails on water at up to {self.max_speed} km/h."


# Stretch goal example:
# Add a new subclass here, such as Train(Vehicle), with its own move() method.


def show_fleet_movement(fleet: list[Vehicle]) -> None:
    for vehicle in fleet:
        message = vehicle.move()
        print(f"{vehicle.__class__.__name__}: {message}")


def main() -> None:
    fleet = [
        Car("Toyota", 180),
        Bike("Trek", 35),
        Boat("Yamaha", 90),
    ]

    show_fleet_movement(fleet)


if __name__ == "__main__":
    main()
