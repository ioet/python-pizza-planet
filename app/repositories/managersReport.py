from typing import Any, List, Optional, Sequence

from app.controllers import ingredient
import sqlalchemy as sq
import json

from .models import Ingredient, Order, OrderDetail, Size, Beverage, db
from .serializers import (IngredientSerializer, OrderSerializer,
                          SizeSerializer, BeverageSerializer, ma)

class BaseManagersReport:
    
    session = db.session
    @classmethod
    def get_most_required(cls):
        query = (
                sq.sql.text("""SELECT  ingredient_id, i.name,  COUNT(ingredient_id) mycount 
                FROM order_detail od JOIN ingredient i ON od.ingredient_id = i."_id" 
                GROUP BY ingredient_id, i.name 
                order by mycount DESC 
                LIMIT 1""")
                ) 
        
        result = cls.session.execute(query)
        return result


    @classmethod   
    def get_beverage_most_required(cls):
        query = (
                sq.sql.text("""SELECT  beverage_id, b.name, COUNT(beverage_id) mycount 
                FROM order_detail od JOIN beverage b ON od.beverage_id = b."_id" 
                GROUP BY beverage_id, b.name
                order by mycount DESC 
                LIMIT 1""")
                ) 
        result = cls.session.execute(query) 
        return result  

    @classmethod
    def get_customers_who_buy_the_most(cls):
        query = (
                sq.sql.text("""SELECT client_name , client_dni ,  SUM(total_price) sum_total
                FROM "order" o GROUP BY client_dni 
                ORDER by sum_total  DESC 
                LIMIT 3""")
                ) 
        result = cls.session.execute(query) 
        return result

    @classmethod
    def get_month_with_most_sales(cls):
        query = (
                sq.sql.text("""SELECT SUM(o.total_price) AS total_mes, strftime('%m', o.date) AS mes FROM "order" o 
                GROUP  BY mes ORDER BY total_mes DESC LIMIT 1""")
                ) 
        result = cls.session.execute(query) 
        return result  



