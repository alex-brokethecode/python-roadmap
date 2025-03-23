# Create a Vehicle class with a fuel_efficiency() abstract method
# - Implement Car and Motorcycle classes with different fuel efficiency calculations.

from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, efficiency: float) -> None:
        self.efficiency = efficiency

    @abstractmethod
    def fuel_efficiency(self,) -> float:
        pass

    def __str__(self) -> str:
        return f"{self.__class__.__name__} with fuel efficiency {self.fuel_efficiency()} km/L"


class Car(Vehicle):
    def __init__(self, efficiency: float) -> None:
        self.__efficiency = efficiency

    def fuel_efficiency(self) -> float:
        return self.__efficiency


class Motorcycle(Vehicle):
    def __init__(self, efficiency: float) -> None:
        self.__efficiency = efficiency

    def fuel_efficiency(self) -> float:
        return self.__efficiency


if __name__ == '__main__':
    car = Car(30)
    motorcycle = Motorcycle(20)

    print(car)
    print(motorcycle)

    print(car.fuel_efficiency())
    print(motorcycle.fuel_efficiency())
