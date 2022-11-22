from unittest import TestCase
import numpy as np
from Points import Point, Points, OrderedPoints, ListToOrderedPoints


class TestPoint(TestCase):

    def test_initialization_with_bad_inputs(self):
        with self.assertRaises(ValueError):
            Point(None, None)
        with self.assertRaises(ValueError):
            Point(5, "abx")
        with self.assertRaises(ValueError):
            Point(True, 1)


class TestPoints(TestCase):

    def test_initialization_with_bad_inputs(self):
        with self.assertRaises(ValueError):
            Points(None)
        with self.assertRaises(ValueError):
            Points([1,2])
        points = Points([Point(2, 1)])

    def test_getLen(self):
        points = Points([Point(2, 1)])
        self.assertEqual(points.getLen(), 1)
        points2 = Points([Point(2, 1), Point(3, 3), Point(4, 0)])
        self.assertEqual(points2.getLen(), 3)

    def test_isOrdered(self):
        points1 = Points([Point(2, 1), Point(3, 3), Point(4, 0)])
        self.assertEqual(points1.isOrdered(), True)
        points2 = Points([Point(2, 1), Point(1, 3), Point(4, 0)])
        self.assertEqual(points2.isOrdered(), False)


class TestOrderedPoints(TestCase):

    def test_initialization_with_bad_inputs(self):
        op = OrderedPoints([Point(2, 1), Point(3, 3), Point(4, 0)])
        with self.assertRaises(ValueError):
            OrderedPoints([Point(2, 1), Point(1, 3), Point(4, 0)])
        with self.assertRaises(ValueError):
            OrderedPoints([Point(2, 1), "sad", Point(4, 0)])
        with self.assertRaises(ValueError):
            OrderedPoints([Point(2, 1), 1, Point(4, 0)])


    def test_getLen(self):
        op = OrderedPoints([Point(2, 1), Point(4, 0)])
        self.assertEqual(op.getLen(), 2)
        op2 = OrderedPoints([Point(2, 1), Point(3, 3), Point(4, 0)])
        self.assertEqual(op2.getLen(), 3)

    def test_getNeighbouringPoints(self):
        op = OrderedPoints([Point(2, 1), Point(3, 3), Point(4, 0)])
        with self.assertRaises(ValueError):
            op.getNeighbouringPoints(np.nan)
        with self.assertRaises(ValueError):
            op.getNeighbouringPoints("sadd")
        with self.assertRaises(ValueError):
            op.getNeighbouringPoints(True)

        val1 = op.getNeighbouringPoints(0)
        val2 = op.getNeighbouringPoints(2.5)
        val3 = op.getNeighbouringPoints(3.6)
        val4 = op.getNeighbouringPoints(10)
        self.assertEqual(val1, OrderedPoints([Point(2, 1)]))
        self.assertEqual(val2, OrderedPoints([Point(2, 1), Point(3, 3)]))
        self.assertEqual(val3, OrderedPoints([Point(3, 3), Point(4, 0)]))
        self.assertEqual(val4, OrderedPoints([Point(4, 0)]))


class TestListToOrderedPoints(TestCase):
    def test_providingBadInputs(self):
        with self.assertRaises(ValueError):
            ListToOrderedPoints([1, 2, 3]) #uneven number of ponts
        with self.assertRaises(ValueError):
            ListToOrderedPoints([1, 2, "s", 4])
        with self.assertRaises(ValueError):
            ListToOrderedPoints([1, 2, True, 4])
        with self.assertRaises(ValueError):
            ListToOrderedPoints([1, 2, None, 4])
        with self.assertRaises(ValueError):
            ListToOrderedPoints([1, 2, np.nan, 4])
        ListToOrderedPoints([1, 2, 3, 4])
