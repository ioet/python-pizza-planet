# import pytest
# from app.data_generator.data_generator import CustomerGenerator, OrderGenerator, IngredientGenerator, SizeGenerator


# from ..utils.functions import *


# def test_customer_generator():
    
#     assert CustomerGenerator.create_dummy_data(
#             customer_address = get_random_string(),
#             customer_dni = get_random_sequence(),
#             customer_name = get_random_string(),
#             customer_phone = get_random_sequence()
#     )

# def test_ingredient_generator():

#     assert IngredientGenerator.create_dummy_data(
#             name = get_random_string(),
#             price = get_random_price(10,20)
#     )


# def test_size_generator():

#     assert SizeGenerator.create_dummy_data(
#             name = get_random_string,
#             price = get_random_price(10,20)
#     )

# def test_order_genarator():

#     assert OrderGenerator.create_dummy_data(
#             customer = CustomerGenerator.create_dummy_data(
#             customer_address = get_random_string(),
#             customer_dni = get_random_sequence(),
#             customer_name = get_random_string(),
#             customer_phone = get_random_sequence()            
#         ),
#         ingredients = IngredientGenerator. create_dummy_data(
#             name = get_random_string(),
#             price = get_random_price(10,20)
#         ),
#         size = SizeGenerator.create_dummy_data(
#             name = get_random_string(),
#             price = get_random_price(10,20)           
#         ), 
#     )