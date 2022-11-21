from abc import ABC, abstractmethod
from typing import List

import numpy as np
from scipy.stats import norm
import pydantic


class UtilityFunction(ABC):
    @abstractmethod
    def GetUtility(self, performance_metric):
        pass
    @abstractmethod
    def GetUtilityFunctionType(self):
        pass

    @abstractmethod
    def GetPerformanceType(self):
        pass


""""
Deifines a linear utility function of the form:
        y = x * a/ b      if x<b
        y = a               if x>b
"""

class ScalingUtilityFunction(UtilityFunction):
    '''' THis constructor exrects list parameters '''

    def __init__(self, param, performanceType):
        if len(param) != 1:
            raise ValueError("There must be one input parameter")
        if np.isnan(param[0]) or param[0] < 0:
            raise ValueError("Input parameter a must be a positive number")

        self.a = param[0]
        self.performanceType = performanceType

    def GetUtility(self, x):
        if np.isnan(x):
            raise ValueError("The utility function input cannot be null")
        if x < 0:
            raise ValueError("The utility function only accepts positive values")

        if np.isnan(x):
            return 0
        if x < 0:
            return 0
        return self.a * x

    def GetUtilityFunctionType(self):
        return "Scaling"

    def GetPerformanceType(self):
        return self.performanceType

class LinearUtilityFunction(UtilityFunction):
    '''' THis constructor expects list parameters '''

    def __init__(self, params, performanceType):
        if len(params) != 2:
            raise ValueError("There must be two input parameters")
        if np.isnan(params[0]) or params[0] < 0:
            raise ValueError("Input parameter a must be a positive number")
        if np.isnan(params[1]) or params[1] < 0:
            raise ValueError("Input parameter b must be a positive number")

        self.a = params[0]
        self.b = params[1]
        self.performanceType = performanceType

    def GetUtility(self, x):
        if np.isnan(x):
            raise ValueError("The utility function input cannot be null")
        if x < 0:
            raise ValueError("The utility function only accepts positive values")

        if np.isnan(x):
            return 0
        if x < 0:
            return 0
        if x < self.b:
            return x * self.a / self.b
        return self.a

    def GetUtilityFunctionType(self):
        return "Linear"

    def GetPerformanceType(self):
        return self.performanceType

class DoubleLinearUtilityFunction(UtilityFunction):
    def __init__(self, params, performanceType):
        if len(params) != 4:
            raise ValueError("There must be four input parameters")
        if np.isnan(params[0]) or params[0] < 0:
            raise ValueError("Input parameter a1 must be a positive number")
        if np.isnan(params[1]) or params[1] < 0:
            raise ValueError("Input parameter b1 must be a positive number")
        if np.isnan(params[2]) or params[2] < 0:
            raise ValueError("Input parameter a2 must be a positive number")
        if np.isnan(params[3]) or params[3] < 0:
            raise ValueError("Input parameter b2 must be a positive number")
        if params[1] > params[3]:
            raise ValueError("Input parameter b2 must be larger than b1")

        self.a1 = params[0]
        self.b1 = params[1]
        self.a2 = params[2]
        self.b2 = params[3]
        self.performanceType = performanceType

    def GetUtility(self, x):
        if np.isnan(x):
            raise ValueError("The utility function input cannot be null")
        if x < 0:
            raise ValueError("The utility function only accepts positive values")

        if np.isnan(x):
            return 0
        if x < 0:
            return 0
        if x < self.b1:
            return x * self.a1 / self.b1
        if x < self.b2:
            return self.a1 + (self.a2 - self.a1) / (self.b2 - self.b1) * (x - self.b1)
        return self.a2

    def GetUtilityFunctionType(self):
        return "DoubleLinear"

    def GetPerformanceType(self):
        return self.performanceType


class NormalCDFUtilityFunction(UtilityFunction):
    def __init__(self, params, performanceType):
        if len(params) != 2:
            raise ValueError("There must be two input parameters")
        if np.isnan(params[0]) or params[0] < 0:
            raise ValueError("Input parameter a must be a positive number")
        if np.isnan(params[1]) or params[1] < 0:
            raise ValueError("Input parameter b must be a positive number")

        self.a = params[0] # represents the max utility in the asymptotic limit
        self.b = params[1] # represents the point where 50% of the max utility is reached
        self.performanceType = performanceType

    def GetUtility(self, x):
        if np.isnan(x):
            raise ValueError("The utility function input cannot be null")
        if x < 0:
            raise ValueError("The utility function only accepts positive values")

        if np.isnan(x):
            return 0
        if x < 0:
            return 0
        if x >= 0:
            return self.a * 2 * (norm.cdf(0.675 * x / self.b)-0.5)

    def GetUtilityFunctionType(self):
        return "NormalCDF"

    def GetPerformanceType(self):
        return self.performanceType

class Point:
    x: float
    y: float

    def __init__(self, x : float, y : float):
        self.x = x
        self.y = y

class Points(List): # TODO: perform implementation test
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
        self.points=points

class OrderedPoints(Points):
    points = List[Point]

    def __init__(self, points: List[Point]):
        if not Points(points).isOrdered():
            raise ValueError("input list is not ordered")
        self.points = points

    def getLen(self):
        return len(self.points)

    def getNeighbouringPoints(self, x: float): #TODO: Construct implementation test
        if len(self.points) == 0:
            return Points([])
        lastPoint = self.points[0]
        if lastPoint.x >= x:
            return Points([lastPoint])
        for point in self.points[1:]:
            if point.x == x: return Points([point])
            if lastPoint.x <= x and point.x >= x: return Points([lastPoint, point])
        return Points([self.points[-1]])

class PerformanceType:
    performanceType: str


class GenericLinearUtilityFunction(UtilityFunction):
    points: Points
    performanceType: PerformanceType
    def __init__(self, points : Points, performanceType: PerformanceType):
        if points.points.__len__() == 0:
            raise ValueError("The list of points is empy")
        if not points.isOrdered():
            raise ValueError("The list of points is not ordered from lowest to highest x-value")
        self.points = points
        self.performanceType = performanceType

    def GetUtility(self, x): # TODO: Construct implementation test
        if np.isnan(x):
            raise ValueError("Input variable cannot be null")
        neighbours = self.points.getNeighbouringPoints(x).points
        if neighbours == []:
            raise ValueError("The utility function has not been given any parameters")
        if len(neighbours) == 1:
            return neighbours[0].y
        p0=neighbours[0]
        p1=neighbours[1]
        return p0.y + (x-p0.x)*(p1.y-p0.y)/(p1.x-p0.x)

    def GetUtilityFunctionType(self):
        return "GenericLinear"

    def GetPerformanceType(self):
        return self.performanceType

a=1

def ListToOrderedPoints(listOfCoordinates : List):
    if listOfCoordinates == None:
        return None
    if len(listOfCoordinates) %2==1:
        raise ValueError("There must be an even number of coordinates")
    #TODO: Make sure that all the inputs are int or float
    l=[listOfCoordinates[i:i + 2] for i in range(0, len(listOfCoordinates), 2)]
    points = []
    for pair in l:
        points.append(Point(pair[0], pair[1]))
    # TODO: check that the list is ordered
    # create the Orderedlist object
    return OrderedPoints(points)
