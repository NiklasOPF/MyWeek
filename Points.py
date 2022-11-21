import math
from abc import ABC, abstractmethod
from typing import List

import numpy as np
from scipy.stats import norm
import pydantic



class Point:
    x: float
    y: float

    def __init__(self, x : float, y : float):
        if x == None or y == None:
            raise ValueError("A point cannot be created if the input parameters are None")
        if (type(x) is not float) and (type(x) is not int):
            raise ValueError("The x variable must be a number")
        if (type(y) is not float) and (type(y) is not int):
            raise ValueError("The y variable must be a number")
        self.x = x
        self.y = y


class Points(List):
    points: List[Point]
    def isOrdered(self):
        if len(self.points) == 0:
            return True
        lastPoint = self.points[0]
        for point in self.points[1:]:
            if point.x <= lastPoint.x:
                return False
        return True

    def getLen(self):
        return len(self.points)

    def __init__(self, points: List[Point]):
        if points == None or points == []:
            raise ValueError("no input provided")
        if (type(points) is not List) and (type(points) is not list):
            raise ValueError("Input must be a list")
        for point in points:
            if type(point) is not Point:
                raise ValueError("components of the list must be of type Point")
        self.points = points



class OrderedPoints(Points):
    points = List[Point]

    def __init__(self, points: List[Point]):
        if not Points(points).isOrdered():
            raise ValueError("input list is not ordered")
        self.points = points

    def getLen(self):
        return len(self.points)

    def getNeighbouringPoints(self, x: float):
        if (type(x) is not float) and (type(x) is not int):
            raise ValueError("the x variable must be a number")
        if x == None or math.isnan(x):
            raise ValueError("the x variable cannot be null")
        if len(self.points) == 0:
            return Points([])
        lastPoint = self.points[0]
        if lastPoint.x >= x:
            return Points([lastPoint])
        for point in self.points[1:]:
            if point.x == x: return Points([point])
            if lastPoint.x <= x and point.x >= x: return Points([lastPoint, point])
        return Points([self.points[-1]])