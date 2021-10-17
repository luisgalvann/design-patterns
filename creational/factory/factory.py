from abc import ABC, abstractstaticmethod


class IShape(ABC):
    ''' Abstract Shape «interface» '''

    @abstractstaticmethod
    def draw() -> None:
        raise NotImplementedError


class Circle(IShape):
    ''' Concrete Shape Circle '''

    def draw(self) -> None:
        print('drawing a circle')


class Square(IShape):
    ''' Concrete Shape Square '''

    def draw(self) -> None:
        print('drawing a square')


class Rectangle(IShape):
    ''' Concrete Shape Rectangle '''

    def draw(self) -> None:
        print('drawing a rectangle')


class ShapeFactory:
    ''' ShapeFactory Implementation '''
    
    @staticmethod
    def getShape(stype: str) -> IShape:
        shape = {
            'circle': Circle(),
            'square': Square(),
            'rectangle': Rectangle(),
        }.get(stype)

        return shape
