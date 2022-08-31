from abc import ABC, abstractmethod
from itertools import product


class DataGenerator(ABC):
    
    @abstractmethod
    def create_dummy_data(self, **kwargs):
        pass




class CustomerGenerator(DataGenerator):

    def create_dummy_data(self, **kwargs):
        pass
        


