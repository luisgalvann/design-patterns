from abc import ABC, abstractstaticmethod


class IShape(ABC):
    ''' Abstract shape «interface» implementation '''

    @abstractstaticmethod
    def draw() -> None:
        raise NotImplementedError


class Circle(IShape):
    ''' Concrete circle class implementation '''

    def draw(self) -> None:
        print('drawing a circle')


class Square(IShape):
    ''' Concrete square class implementation '''

    def draw(self) -> None:
        print('drawing a square')


class Rectangle(IShape):
    ''' Concrete rectangle class implementation '''

    def draw(self) -> None:
        print('drawing a rectangle')


class ShapeFactory:
    ''' ShapeFactory class implementation '''
    
    @staticmethod
    def getShape(stype: str) -> IShape:
        shape = {
            'circle': Circle(),
            'square': Square(),
            'rectangle': Rectangle(),
        }.get(stype)

        return shape
