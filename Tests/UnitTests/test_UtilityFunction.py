from unittest import TestCase
from UtilityFunctions.UtilityFunction import NormalCDFUtilityFunction
import numpy as np


class TestNormalCDFUtilityFunction(TestCase):

    def test_get_utility(self):
        utilityFun = NormalCDFUtilityFunction([10, 2], "Test")
        self.assertEqual(utilityFun.GetUtility(2), 5.0032423505644585)
        self.assertEqual(utilityFun.GetUtility(-1), 0)
        self.assertEqual(utilityFun.GetUtility(np.nan), 0)
        self.assertEqual(utilityFun.GetUtility(1000), 10)
