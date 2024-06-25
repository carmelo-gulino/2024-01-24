from database.DB_connect import DBConnect
from model.method import Method
from model.product import Product


class DAO:
    def __init__(self):
        pass

    @staticmethod
    def get_all_methods():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select * from go_methods gm order by gm.Order_method_type """
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(Method(**row))
        cursor.close()
        cnx.close()
        return result

    @staticmethod
    def get_nodes(year, method):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select gp.* , sum(gds.Unit_sale_price * gds.Quantity) ricavo_tot
                    from go_products gp , go_daily_sales gds 
                    where gp.Product_number = gds.Product_number and year(gds.`Date`) = %s and gds.Order_method_code = %s
                    group by gp.Product_number """
        cursor.execute(query, (year, method))
        result = []
        for row in cursor:
            result.append(Product(**row))
        cursor.close()
        cnx.close()
        return result
