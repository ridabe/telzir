from app.Model import telzirSqliteModel
from app.Interface import plansInteface
import pandas as pd


class PlansRepository(plansInteface.PlansInteface):
    def getPlans(self):

        query = """
            Select * from plans
        """
        response = telzirSqliteModel.cursor_obj.execute(query)
        response = telzirSqliteModel.cursor_obj.fetchall()
        return response

    def get_minuts_by_id(self, planId):
        response = telzirSqliteModel.cursor_obj.execute(" Select minuts from plans where id = ?", (planId))
        telzirSqliteModel.cursor_obj.close()
        return response

    def get_price_call(self, origin, destiny):
        response = telzirSqliteModel.cursor_obj.execute(
            "Select price from values_call where origin = ? and destiny = ?", (origin, destiny))
        response = telzirSqliteModel.cursor_obj.fetchall()
        return response

    def get_area_code(self):
        query = """
                    Select * from area_code
                """
        response = telzirSqliteModel.cursor_obj.execute(query)
        response = telzirSqliteModel.cursor_obj.fetchall()
        return response

    def get_call_time(self):
        query = """
                 Select time from call_time
                """
        response = telzirSqliteModel.cursor_obj.execute(query)
        response = telzirSqliteModel.cursor_obj.fetchall()
        return response

