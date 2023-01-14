from typing import Type
from app.Interface import plansInteface


class PlansService:
    def __init__(self, repository: Type[plansInteface.PlansInteface]):
        self.__repository = repository

    def get_plans(self):
        plans = self.__repository.getPlans(self)
        return plans

    def get_area_code(self):
        code = self.__repository.get_area_code(self)
        return code

    def get_call_time(self):
        time = self.__repository.get_call_time(self)
        return time

    def get_price_call(self, origin, destiny):
       price = self.__repository.get_price_call(self, origin, destiny)
       return price
