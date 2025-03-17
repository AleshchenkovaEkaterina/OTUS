from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

   @abstractmethod
    def add_area(self):
        if isinstance(figure, Figure):
            return self.get_area() + figure.get_area()
        else: raise ValueError("There is no figure")
