from management.product_handler import get_product_by_id
from management.product_handler import get_products_by_type
from management.product_handler import add_product
from management.product_handler import menu_report
from menu import products

if __name__ == "__main__": 
  print(get_product_by_id(28))
  print(get_products_by_type('drink'))
  new_product = {
        "title": "X-Python",
        "price": 5.0,
        "rating": 5,
        "description": "Sanduiche de Python",
        "type": "fast-food"
    }
  table_1 = [{"_id": 1, "amount": 5}, {"_id": 19, "amount": 5}]
  table_2 = [
        {"_id": 10, "amount": 3},
        {"_id": 20, "amount": 2},
        {"_id": 21, "amount": 5},
    ]
  print(add_product(products, **new_product))
  print(menu_report())
  

