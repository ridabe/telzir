from abc import ABC, abstractmethod

class PlansInteface(ABC):

    @abstractmethod
    def getPlans(self):
        pass

    @abstractmethod
    def get_minuts_by_id(self, planId):
       pass

    @abstractmethod
    def get_price_call(self, origin, destiny):
       pass

    @abstractmethod
    def get_area_code(self):
        pass

    @abstractmethod
    def get_call_time(self):
        pass