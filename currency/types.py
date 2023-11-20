from abc import ABC, abstractmethod


class ModelDataCreator(ABC):
    @abstractmethod
    def create_model_data(self, *args, **kwargs):
        pass
