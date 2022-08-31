from abc import ABC, abstractmethod

class DataGenerator(ABC):
    
    @abstractmethod
    def create_dummy_data(**kwargs):
        pass


class CustomerGenerator(DataGenerator):

    def create_dummy_data(customer_address, customer_dni, customer_name, customer_phone):
        new_customer = {
            'customer_address': customer_address,
            'customer_dni': customer_dni,
            'customer_name': customer_name,
            'customer_phone': customer_phone
        }
        return new_customer
    
