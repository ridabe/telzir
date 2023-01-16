from app import app, request, os
from app.Service import planCalculateService as pc
from app.Service import plansService as ps
import unittest




class TestPlanCalculateService(unittest.TestCase):

    def test_shoud_return_value_without_plan(self):
        origin = 11
        destiny = 17
        time_call = 80
        plan = 60
        price = 1.70
        response = pc.calculate_without_plan(time_call, price) # 136
        expected = 136
        self.assertEqual(response, expected)

    def test_shoud_return_value_with_plan(self):
        surplusMin = 20
        indemnityPrice = 1.87
        response = round(pc.calculate_with_plan(surplusMin, indemnityPrice),2)
        expected = 37.4
        self.assertEqual(response, expected)

    def test_shoud_calculate_indemnity(self):
        price = 1.70
        expected = 1.87
        response = pc.calculate_indemnity(price)
        self.assertEqual(response, expected)

    def test_shoud_calculate_surplus(self):
        time_call = 80
        plan = 60
        expected = 20
        response = pc.calculate_surplus(time_call, plan)
        self.assertEqual(response, expected)

if __name__ == "__name__":
    unittest.main