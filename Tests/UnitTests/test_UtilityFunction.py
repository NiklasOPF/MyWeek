from unittest import TestCase
from UtilityFunctions.UtilityFunction import NormalCDFUtilityFunction, DoubleLinearUtilityFunction, \
    LinearUtilityFunction, ScalingUtilityFunction, GenericLinearUtilityFunction, Point, OrderedPoints, Points
import numpy as np


class TestNormalCDFUtilityFunction(TestCase):

    def test_initialization_with_no_inputs(self):
        with self.assertRaises(ValueError):
            NormalCDFUtilityFunction([], "Test")

    def test_initialization_with_negative_inputs(self):
        with self.assertRaises(ValueError):
            NormalCDFUtilityFunction([-10, -2], "Test")

    def test_initialization_with_null_inputs(self):
        with self.assertRaises(ValueError):
            NormalCDFUtilityFunction([10, np.nan], "Test")

    def test_get_utility(self):
        utilityFun = NormalCDFUtilityFunction([10, 2], "Test")
        self.assertEqual(utilityFun.GetUtility(2), 5.0032423505644585)
        with self.assertRaises(ValueError):
            utilityFun.GetUtility(-1)
        with self.assertRaises(ValueError):
            utilityFun.GetUtility(np.nan)
        self.assertEqual(utilityFun.GetUtility(1000), 10)

    def test_get_utility_function_type(self):
        utilityFun = NormalCDFUtilityFunction([10, 2], "Test")
        self.assertEqual(utilityFun.GetUtilityFunctionType(), "NormalCDF")


class TestDoubleLinearUtilityFunction(TestCase):

    def test_initialization_with_no_inputs(self):
        with self.assertRaises(ValueError):
            DoubleLinearUtilityFunction([], "Test")

    def test_initialization_with_bad_inputs(self):
        with self.assertRaises(ValueError):
            DoubleLinearUtilityFunction([5, 3, 10, 2], "Test")
        with self.assertRaises(ValueError):
            DoubleLinearUtilityFunction([-5, 1, 10, 2], "Test")
        with self.assertRaises(ValueError):
            DoubleLinearUtilityFunction([5, -3, 10, 2], "Test")
        with self.assertRaises(ValueError):
            DoubleLinearUtilityFunction([5, 3, -10, 2], "Test")
        with self.assertRaises(ValueError):
            DoubleLinearUtilityFunction([5, 3, 10, -2], "Test")
        with self.assertRaises(ValueError):
            DoubleLinearUtilityFunction([5, 3], "Test")
        with self.assertRaises(ValueError):
            DoubleLinearUtilityFunction([5, 3, 6, 4, 7], "Test")

    def test_get_utility(self):
        utilityFun = DoubleLinearUtilityFunction([5, 3, 10, 5], "Test")
        with self.assertRaises(ValueError):
            utilityFun.GetUtility(-1)
        with self.assertRaises(ValueError):
            utilityFun.GetUtility(np.nan)
        self.assertEqual(utilityFun.GetUtility(0), 0)
        self.assertEqual(utilityFun.GetUtility(1.5), 2.5)
        self.assertEqual(utilityFun.GetUtility(2), 2 * 5 / 3)
        self.assertEqual(utilityFun.GetUtility(3), 5)
        self.assertEqual(utilityFun.GetUtility(4), 7.5)
        self.assertEqual(utilityFun.GetUtility(5), 10)
        self.assertEqual(utilityFun.GetUtility(7), 10)
        self.assertEqual(utilityFun.GetUtility(1000), 10)


class TestLinearUtilityFunction(TestCase):

    def test_initialization_with_no_inputs(self):
        with self.assertRaises(ValueError):
            LinearUtilityFunction([], "Test")

    def test_initialization_with_bad_inputs(self):
        with self.assertRaises(ValueError):
            LinearUtilityFunction([-5, 3], "Test")
        with self.assertRaises(ValueError):
            LinearUtilityFunction([5, -3], "Test")
        with self.assertRaises(ValueError):
            LinearUtilityFunction([5], "Test")
        with self.assertRaises(ValueError):
            LinearUtilityFunction([5, 3, 4], "Test")

    def test_get_utility(self):
        utilityFun = LinearUtilityFunction([5, 3], "Test")
        with self.assertRaises(ValueError):
            utilityFun.GetUtility(-1)
        with self.assertRaises(ValueError):
            utilityFun.GetUtility(np.nan)
        self.assertEqual(utilityFun.GetUtility(0), 0)
        self.assertEqual(utilityFun.GetUtility(0.5), 5 / 6)
        self.assertEqual(utilityFun.GetUtility(1), 5 / 3)
        self.assertEqual(utilityFun.GetUtility(1.5), 2.5)
        self.assertEqual(utilityFun.GetUtility(2.999999999999999999), 5)
        self.assertEqual(utilityFun.GetUtility(3.1), 5)
        self.assertEqual(utilityFun.GetUtility(10), 5)
        self.assertEqual(utilityFun.GetUtility(1000000000), 5)


class TestScalingUtilityFunction(TestCase):
    def test_initialization_with_no_inputs(self):
        with self.assertRaises(ValueError):
            ScalingUtilityFunction([], "Test")

    def test_initialization_with_bad_inputs(self):
        with self.assertRaises(ValueError):
            ScalingUtilityFunction([-5], "Test")
        with self.assertRaises(ValueError):
            ScalingUtilityFunction([5, 3], "Test")

    def test_get_utility(self):
        utilityFun = ScalingUtilityFunction([5], "Test")
        with self.assertRaises(ValueError):
            utilityFun.GetUtility(-1)
        with self.assertRaises(ValueError):
            utilityFun.GetUtility(np.nan)
        self.assertEqual(utilityFun.GetUtility(0), 0)
        self.assertEqual(utilityFun.GetUtility(0.5), 2.5)
        self.assertEqual(utilityFun.GetUtility(1000), 5000)


class TestNormalCDFUtilityFunction(TestCase):

    def test_initialization_with_no_inputs(self):
        with self.assertRaises(ValueError):
            NormalCDFUtilityFunction([], "Test")

    def test_initialization_with_bad_inputs(self):
        with self.assertRaises(ValueError):
            NormalCDFUtilityFunction([-5, 3], "Test")
        with self.assertRaises(ValueError):
            NormalCDFUtilityFunction([5, -3], "Test")
        with self.assertRaises(ValueError):
            NormalCDFUtilityFunction([5, 3, 4], "Test")

    def test_get_utility(self):
        utilityFun = NormalCDFUtilityFunction([5, 3], "Test")
        with self.assertRaises(ValueError):
            utilityFun.GetUtility(-1)
        with self.assertRaises(ValueError):
            utilityFun.GetUtility(np.nan)
        f=utilityFun.GetUtility(0)
        self.assertEqual(utilityFun.GetUtility(0), 0)
        self.assertEqual(utilityFun.GetUtility(1.5), 1.3212999392852298) #slightly larger than 2.5 / 2 = 1.25
        self.assertEqual(utilityFun.GetUtility(3), 2.5016211752822306)
        self.assertEqual(utilityFun.GetUtility(4.5), 3.443504766532315) #slightly smaller than 2.5 + (2.5 / 2) = 3.75
        self.assertEqual(utilityFun.GetUtility(1000000000), 5)





class TestGenericLinearUtilityFunction(TestCase):

    def test_initialization_with_no_inputs(self):
        with self.assertRaises(ValueError):
            GenericLinearUtilityFunction([], "Test")

    def test_get_utility(self):
        utilityFun1 = GenericLinearUtilityFunction(OrderedPoints([Point(3,5)]), "Test")
        with self.assertRaises(ValueError):
            utilityFun1.GetUtility(np.nan)
        self.assertEqual(utilityFun1.GetUtility(0), 5)
        self.assertEqual(utilityFun1.GetUtility(3), 5)
        self.assertEqual(utilityFun1.GetUtility(10), 5)

        utilityFun2 = GenericLinearUtilityFunction(OrderedPoints([Point(3,5), Point (5,7)]), "Test")
        with self.assertRaises(ValueError):
            utilityFun2.GetUtility(np.nan)
        self.assertEqual(utilityFun2.GetUtility(0), 5)
        self.assertEqual(utilityFun2.GetUtility(3), 5)
        self.assertEqual(utilityFun2.GetUtility(4), 6)
        self.assertEqual(utilityFun2.GetUtility(4.5), 6.5)
        self.assertEqual(utilityFun2.GetUtility(5), 7)
        self.assertEqual(utilityFun2.GetUtility(8), 7)
        self.assertEqual(utilityFun2.GetUtility(10), 7)
        self.assertEqual(utilityFun2.GetUtility(1000000000), 7)

        with self.assertRaises(ValueError):
            utilityFun3 = GenericLinearUtilityFunction(OrderedPoints([Point (5,7), Point(3,5)]), "Test")
