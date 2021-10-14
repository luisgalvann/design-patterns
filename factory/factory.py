from abc import ABC, abstractmethod


class Shape(ABC):
    ''' Abstract Shape «interface» '''

    @staticmethod  # This way it doesn't need 'self'
    @abstractmethod
    def draw() -> None:
        raise NotImplementedError


class Circle(Shape):
    ''' Concrete Shape Circle '''

    def draw(self) -> None:
        print('drawing a circle')


class Square(Shape):
    ''' Concrete Shape Square '''

    def draw(self) -> None:
        print('drawing a square')


class Rectangle(Shape):
    ''' Concrete Shape Rectangle '''

    def draw(self) -> None:
        print('drawing a rectangle')


class ShapeFactory:
    ''' ShapeFactory Implementation '''
    
    @staticmethod
    def getShape(choice: str) -> Shape:
        shape = {
            'circle': Circle(),
            'square': Square(),
            'rectangle': Rectangle(),
        }.get(choice)

        return shape
